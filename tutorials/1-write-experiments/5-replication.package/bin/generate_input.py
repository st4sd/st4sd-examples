#!/usr/bin/env python

import random
import yaml
import sys

random.seed(int(sys.argv[1]))

numbers = [
    random.randint(int(sys.argv[2]), int(sys.argv[3])),
    random.randint(int(sys.argv[2]), int(sys.argv[3]))
]

with open(sys.argv[4], "wt") as f:
    yaml.safe_dump(numbers, f)
