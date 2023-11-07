# ST4SD Examples

This repository contains notebooks illustrating how to use ST4SD APIs to launch, query, and retrieve experiment results. 

## Quick links

- [Available notebooks](#available-notebooks)
- [Requirements](#requirements)
- [Running via CLI](#running-via-cli)
- [Running via a container](#running-via-a-container)
- [Help and Support](#help-and-support)
- [Contributing](#contributing)
- [License](#license)


## Available notebooks

In the [notebooks](notebooks) folder you will find:

- [ST4SD Runtime API Example](notebooks/ST4SD%20Runtime%20API%20Example.ipynb)
  - Illustrates the Runtime APIs used for launching, monitoring and retrieve high level results
- [ST4SD Datastore - Common Query Examples](notebooks/ST4SD%20Datastore%20-%20Common%20Query%20Examples.ipynb)
  - Illustrates the Datastore APIs used for more intricate querying and arbitrary information retrieval
- [ST4SD Runtime API Property Retrieval](notebooks/ST4SD%20Runtime%20API%20Property%20Retrieval.ipynb)
   - Illustrates ways to retrieve properties measured by the experiments
- [bite-size examples for using python wrappers to the ST4DS REST-APIs](notebooks/bites)

## Requirements

These notebooks require `st4sd-runtime-core` to be installed.

You can follow the instructions in the [`st4sd-runtime-core`](https://github.com/st4sd/st4sd-runtime-core#local) repository to install it locally with Jupyter support and proceed to [running via CLI](#running-via-cli), or skip to [running via a container](#running-via-a-container) to use a pre-built container image.

**NOTE**: ST4SD requires authentication to be used and the notebooks will guide you on how to do it. To limit the chances of the tokens being stored in the notebook and pushed somewhere we make use of the Password IPython widget. Visual Studio Code, however, currently does not seem to allow pasting in the rendered Password input. If you want to use VSCode, paste your token in the cell that follows it, but **make sure to remove it before pushing or sharing your notebooks**!

## Running via CLI

**NOTE**: Ensure that if you installed `st4sd-runtime-core` into a virtual environment, it is activated.

1. Clone the repository locally using

  ```bash
  git clone https://github.com/st4sd/st4sd-examples.git
  ```

  Or, if you prefer to use SSH cloning:

  ```bash
  git clone git@github.com:st4sd/st4sd-examples.git
  ```

2. Change into the directory you just cloned

  ```bash
  cd st4sd-examples
  ```

3. Start the Jupyter notebook (in this example "ST4SD Runtime API Example.ipynb")

  ```bash
  jupyter-notebook "notebooks/ST4SD Runtime API Example.ipynb"
  ```

## Running via a container

1. Clone the repository locally using

  ```bash
  git clone https://github.com/st4sd/st4sd-examples.git
  ```

  Or, if you prefer to use SSH cloning:

  ```bash
  git clone git@github.com:st4sd/st4sd-examples.git
  ```

2. Change into the directory you just cloned

  ```bash
  cd st4sd-examples
  ```

3. Pull the `st4sd-runtime-core` container image

  ```bash
  docker pull quay.io/st4sd/official-base/st4sd-runtime-core
  ```

4. Start the container

  **NOTE**: the following command assumes that port 8888 is free.

  ```bash
  docker run -w /st4sd-examples --rm -it -v $PWD:/st4sd-examples -p 8888:8888 quay.io/st4sd/official-base/st4sd-runtime-core jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
  ```

You can now find the notebooks at one of the addresses that are printed out by the container (use the token provided at the end of the string to authenticate).

## Help and Support

Please feel free to reach out to one of the maintainers listed in the [MAINTAINERS.md](MAINTAINERS.md) page.

## Contributing 

We always welcome external contributions. Please see our [guidance](CONTRIBUTING.md) for details on how to do so.

## References

If you use ST4SD in your projects, please consider citing the following:

```bibtex
@software{st4sd_2022,
author = {Johnston, Michael A. and Vassiliadis, Vassilis and Pomponio, Alessandro and Pyzer-Knapp, Edward},
license = {Apache-2.0},
month = {12},
title = {{Simulation Toolkit for Scientific Discovery}},
url = {https://github.com/st4sd/st4sd-runtime-core},
year = {2022}
}
```

## License

This project is licensed under the Apache 2.0 license. Please [see details here](LICENSE.md).