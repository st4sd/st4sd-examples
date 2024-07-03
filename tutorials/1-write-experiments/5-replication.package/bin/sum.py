#!/usr/bin/env python

import yaml
import sys

with open(sys.argv[1], "rt") as f:
    s = sum(yaml.safe_load(f))

replica = sys.argv[2]

print(f"Replica {replica} computed sum {s}")

with open("sum", "wt") as f:
    f.write(str(s))
