#works only with three address code format

import re


class CommonSubExpression:

	def __init__(self, fname):
		self.fname = fname

	def run_optim(self):

		identifier = "(([a-z]|[A-Z]|_)+=([A-Z]|[a-z]|[0-9])[\+\-\*\/]([a-z]|[A-Z]|[0-9])$)"
		identifier = re.compile(identifier)

		subexpr = "(([a-z]|[A-Z])+[\+\-\*\/]([A-Z]|[a-z])+)"
		subexpr = re.compile(subexpr)

		expr_dict = {}

		f = open(self.fname, "r")
		lines = f.readlines()
		f.close()

		for i in range(len(lines)):
			if identifier.search(lines[i]):
				lhs = lines[i].split('=')[0]
				rhs = lines[i].split('=')[1].strip("\n")

				expr_dict[rhs] = lhs
				#print(expr_dict)	
			
			elif subexpr.findall(lines[i]):
				lst = subexpr.findall(lines[i])
				for elem in lst:
					if elem[0] in expr_dict:
						lines[i] = lines[i].replace(elem[0], expr_dict[elem[0]])

			

		f = open("optim1.py", "w")
		f.writelines(lines)
		f.close()



