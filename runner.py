from constant_propagation import ConstantPropagation as cp
from strength_red import StrengthReduction as sr
from const_folding import ConstantFolding as cf

strred = sr("test2.py")
strred.run_optim()
print("completed strength reduction")

consprop = cp("optim2.py")
consprop.run_optim()
print("completed constant_propagation")

consfold = cf("optimizer.py")
consfold.run_optim()
print("completed const_folding")


consprop = cp("optim3.py")
consprop.run_optim()

print("completed second epoch of constant_propagation")


consfold = cf("optimizer.py")
consfold.run_optim()
print("completed second epoch of const_folding")


consprop = cp("optim3.py")
consprop.run_optim()

print("completed third epoch of constant_propagation")
