from constant_propagation import ConstantPropagation as cp
from strength_red import StrengthReduction as sr
from const_folding import ConstantFolding as cf
from common_subexpr import CommonSubExpression as commn

print("Welcome to Python Code Optimization module")
fname = input("Enter the python filename to be optimized: ")



cexpr = commn(fname)
cexpr.run_optim()
print("Completed Elimination of common subexpression")
print("File after Elimination of common subexpression is available at optim1.py ")
print()

strred = sr("optim1.py")
strred.run_optim()
print("completed strength reduction")
print("File after Strength Reduction is available at optim2.py ")
print()

consprop = cp("optim2.py")
consprop.run_optim()
print("completed first epoch of constant propagation")

consfold = cf("optim3.py")
consfold.run_optim()
print("completed first epoch of constant folding")


consprop = cp("optimizer.py")
consprop.run_optim()
print("completed second epoch of constant propagation")

print("File after Constant propagation is available at optim3.py ")
print()


consfold = cf("optim3.py")
consfold.run_optim()
print("completed second epoch of constant folding")


print()
print()
print("Optimization process complete")
print("The optimized code is available in the file optimizer.py")
