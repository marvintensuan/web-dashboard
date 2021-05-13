from numpy import linspace
from numpy.random import uniform

from sympy.parsing.sympy_parser import eval_expr

import numpy
numpy_dict = {a: getattr(numpy,a) for a in dir(numpy)}

def approx(f, a, b, c, d, size):
    xs = uniform(a, b, size)
    ys = uniform(c, d, size)

    under = ys < eval_expr(f, {'xs: xs', numpy_dict})

    return sum(under) / size * area