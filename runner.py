from constant_propagation import ConstantPropagation as cp
from strength_red import StrengthReduction as sr

strred = sr("test2.py")
strred.run_optim()

consprop = cp("optim2.py")
consprop.run_optim()

