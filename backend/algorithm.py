from numpy import linspace
from numpy.random import uniform

from sympy.parsing.sympy_parser import eval_expr

import numpy
numpy_dict = {a: getattr(numpy,a) for a in dir(numpy)}

def approx(f, a, b, c, d, size):
    xs = uniform(a, b, size)
    ys = uniform(c, d, size)

    area = (d-c) * (b-a)
    under = ys < eval_expr(f, {'xs': xs}, numpy_dict)

    return sum(under) / size * area

if __name__ == '__main__':
    # python .\backend\algorithm.py 'sqrt(4 - xs**2)' 0 2 0 2
    from sys import argv
    f, a, b, c, d = argv[1:6]
    size = int(argv[6]) if len(argv) == 7 else 100
    a, b, c, d = map(int, (a, b, c, d))

    print(f'Integrating {f} from {a} to {b} with {size} samples.')
    result = approx(f, a, b, c, d, size)
    print(f'{result = }')