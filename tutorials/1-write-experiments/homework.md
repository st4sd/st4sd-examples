Implement a workflow, which:

1. Has the name: “calculate-sum-of-products”
2. Has 3 arguments:
    - `input.numbers.json`: input file pointing to a JSON file containing an array. Each value of the array is an array of integers.
    - `index_start`: An integer indicating the starting index of numbers.json to process
    - `length`: An integer indicating how many arrays from numbers.json to process starting from index_start
3. The workflow should use “replicate” to produce 1 JSON file per sub-array of “input.numbers.json” for each of the arrays whose index falls within [index_start, index_start + length)
4. The workflow should use multiple step to calculate the product of the numbers. Each step should consume one of the arrays and stores the array's product under a file called “product.json”.
5. The workflow should use “aggregate” for a step called “sum_products” which calculates the sum the products that the above component replicas produced. “sum-products” should store the sum of the products under the file “sum_of_products.json”

This workflow emulates some of the patterns we've seen workflow developers use. Often, workflows process a large number of inputs in parallel (this is where the "replicate" part comes into play) and have some kind of analysis at the end which "aggregates" the results of the parallel computations.

There's no need to try and get it 100% right in one go! The goal here is for you get familiarized with implementing your own workflows. We recommend starting by thinking how you would provide input to the individual replicas. In fact, there are a couple of different ways you can go about that. Next, implement your workflow and use the [`check_homework.py`](check_homework.py) script till you get it right!
