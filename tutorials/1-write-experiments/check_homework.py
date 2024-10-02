#!/usr/bin/env python3

"""
Here is a script you can use to check your "homework" for the group of tutorials in `1-write-experiments`
"""

import json
import os
import shutil
import time
import typing
import functools
import random
import uuid
import subprocess
from typing_extensions import Annotated

import typer

import yaml


def calculate_answer(
    numbers: typing.List[typing.List[int]], index_start: int, length: int
) -> int:
    return sum(
        functools.reduce(lambda agg, x: agg * x, array, 1)
        for array in numbers[index_start : index_start + length]
    )


def generate_values(
    max_length: int, entry_length: int
) -> typing.List[typing.List[int]]:
    return [
        [random.randint(1, 10) for _ in range(entry_length)] for _ in range(max_length)
    ]


def sanity_check_workflow(path_to_workflow: str):
    """Very rough sanity checking on the definition of the workflow"""
    import experiment.model.conf
    import experiment.model.storage

    conf = (
        experiment.model.conf.ExperimentConfigurationFactory.configurationForExperiment(
            path_to_workflow,
            createInstanceFiles=False,
        )
    )

    if not isinstance(conf, experiment.model.conf.DSLExperimentConfiguration):
        raise ValueError("The workflow does not use the DSL 2.0 syntax")

    # VV: just to keep the linter happy
    conf = typing.cast(experiment.model.conf.DSLExperimentConfiguration, conf)

    dsl = conf.dsl_namespace

    wf_name = dsl.entrypoint.entryInstance
    workflow = [w for w in dsl.workflows if w.signature.name == wf_name]

    if len(workflow) != 1:
        raise ValueError("The entrypoint does not point to a Workflow")

    workflow = workflow[0]

    if workflow.signature.name != "calculate-sum-of-products":
        raise ValueError(
            "entry-instance workflow is not called calculate-sum-of-products"
        )

    if "sum-products" not in workflow.steps:
        raise ValueError("Workflow is missing a step called calc-products")

    exec_sum_products = [e for e in workflow.execute if e.target == "<calc-products>"]
    if len(exec_sum_products) != 1:
        raise ValueError(
            "Your workflow contains multiple copies of the step called calc-products"
        )


def execute_workflow(
    path: str,
    values: typing.Optional[typing.List[typing.List[int]]],
    cleanup_on_success: bool,
):
    """Executes the workflow and validates the value it computes"""
    max_length = 10
    index_start = random.randint(1, max_length - 1)
    length = random.randint(1, max_length - index_start)

    if values is None:
        values = generate_values(max_length, 4)

    variables = {
        "global": {
            "length": length,
            "index_start": index_start,
        }
    }

    instance_name = f"exercise-{uuid.uuid4()}"
    path_instance = f"{instance_name}.instance"

    with open("numbers.json", "w", encoding="utf-8") as f:
        json.dump(values, f)

    with open("variables.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(variables, f)

    print(f"Will run {path} with")
    print("Contents of numbers.json")
    print(json.dumps(values))
    print("Contents of variables.yaml")
    print(yaml.safe_dump(variables), end="")

    cmdline_args = [
        "elaunch.py",
        "-i",
        "numbers.json",
        "-a",
        "variables.yaml",
        "--nostamp",
        "--instanceName",
        instance_name,
        path,
    ]

    proc = subprocess.Popen(
        cmdline_args,
        env=os.environ,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    proc.wait()

    if proc.returncode != 0:
        raise ValueError(
            f"Experiment did not Finish, troubleshoot your experiment instance {path_instance}"
        )

    try:
        with open(
            os.path.join(
                path_instance,
                "stages",
                "stage0",
                "sum-products",
                "sum_of_products.json",
            ),
            "r",
            encoding="utf-8",
        ) as f:
            result = json.load(f)
    except FileNotFoundError:
        raise ValueError(
            "Your step sum-products did not produce the file sum_of_products.json"
        )

    solution = calculate_answer(values, index_start=index_start, length=length)

    if solution != result:
        raise ValueError(
            f"Your step sum-products computed the wrong answer {result} instead of {solution}"
        )

    print("Run computed the correct value", solution, "\n")

    if cleanup_on_success:
        # VV: housekeeping
        shutil.rmtree(path_instance, ignore_errors=True)
        os.remove("variables.yaml")
        os.remove("numbers.json")


def main(
    path: Annotated[str, typer.Option(help="The path to your experiment")],
    seed: Annotated[
        typing.Optional[int],
        typer.Option(
            help="The seed to use for your experiments. "
            "If unset will be auto generated"
        ),
    ] = None,
    number_tests: Annotated[int, typer.Option(help="How many tests to run")] = 3,
    cleanup_on_success: Annotated[
        bool,
        typer.Option(
            help="Whether to delete intermediate files and directories on a successful run"
        ),
    ] = True,
):
    if number_tests < 0:
        raise ValueError("number_tests must be positive")

    sanity_check_workflow(path)

    if seed is None:
        seed = int(time.time())

    print("Seed for the runs", seed)
    random.seed(seed)

    # VV: Try a couple different inputs
    for _ in range(number_tests):
        execute_workflow(path, values=None, cleanup_on_success=cleanup_on_success)

    print("Congratulations! Your experiment works as expected")


if __name__ == "__main__":
    typer.run(main)
