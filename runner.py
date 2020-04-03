from constant_propagation import ConstantPropagation as cp
from strength_red import StrengthReduction as sr

consprop = cp("test.py")
consprop.run_optim()

strred = sr("test2.py")
strred.run_optim()