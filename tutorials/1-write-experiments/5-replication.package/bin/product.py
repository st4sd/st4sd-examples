#!/usr/bin/env python

import numpy
import sys

product = numpy.prod([int(x) for x in sys.argv[1:]])
print(product)