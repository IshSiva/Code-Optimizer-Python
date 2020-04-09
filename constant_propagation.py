import re


class ConstantPropagation:

    def __init__(self, fname):
        self.fname = fname


    def run_optim(self):
        id_pat = "([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9])*=(([a-z]|[A-Z]|[0-9]+)|(\"\w+\"))"
        id_pat = re.compile(id_pat)
        f = open(self.fname, "r")
        lines = f.readlines()
        f.close()
        for line_num in range(len(lines)):

            if id_pat.search(lines[line_num]):

                lines[line_num] = lines[line_num].strip("\n")
                lhs = lines[line_num].split("=")[0]
                rhs = lines[line_num].split("=")[1]
                #print(lhs,rhs)

                if(lhs not in rhs):
                    for rep in range(line_num+1, len(lines)):
                        if id_pat.search(lines[rep]):
                            #print(lhs,lines[rep].split("=")[0] )
                            if lhs == lines[rep].split("=")[0]:
                                if lhs in lines[rep].split("=")[1]:
                                    
                                    #print(lines[rep].split("=")[1].replace(lhs,rhs))

                                    nstr = lines[rep].split("=")[1].replace(lhs,rhs)
                                    
                                    lines[rep] = lines[rep].split("=")[0]+"="+nstr
                                    #print(lines[rep])

                                    
                                break


                            elif lhs in lines[rep].split("=")[1]:

                                nstr = lines[rep].split("=")[1].replace(lhs,rhs)
                                #print(lhs,nstr)
                                lines[rep] = lines[rep].split("=")[0]+"="+nstr
                                #print(lhs, lines[rep])

                lines[line_num]+="\n"

        f = open("optim3.py", "w")
        f.writelines(lines)
        f.close()

