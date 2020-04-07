import re


class ConstantFolding:
	def __init__(self, fname):
		self.fname = fname


	def run_optim(self):

		f = open(self.fname, "r")
		lines = f.readlines()
		f.close()

		pat ="([0-9]+[\+\-\*\/][0-9]+([\+\-\*\/][0-9]+)*)"
		pat = re.compile(pat)

		for j in range(len(lines)):

			if(pat.search(lines[j])):
				s = lines[j]
				lst = pat.findall(s)
				

				for i in lst:
					olstr = i[0]

					nstr = eval(olstr)
					
					s = s.replace(olstr, str(nstr))
			
				lines[j] = s


		f= open("optimizer.py", "w")
		f.writelines(lines)
		f.close()

