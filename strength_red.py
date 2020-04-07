import re 


class StrengthReduction:

    def __init__(self, fname):
        self.fname = fname


    def run_optim(self):

        f = open(self.fname, "r")
        lines = f.readlines()
        

        s="([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9])*\=([a-z]|[A-Z]|[0-9])+((\*)|(\*\*))([0-9])+"
        s=re.compile(s)

        #print(lines)
        for j in range(len(lines)):
            if(s.search(lines[j])):
                #print(lines[j])
                rhs = lines[j].split('=')[1]


                if '**' in rhs:
                    val = int(rhs.split('**')[1])
                    try:
                        lhsval = int(rhs.split('**')[0])
                    except:
                        lhsval = rhs.split('**')[0]
                    
                    if(type(lhsval) == int):
                        ans=lhsval
                        for i in range(val-1):
                            ans*=lhsval

                    else:
                        ans = lhsval+"*"
                        for i in range(val-2):
                            ans+=lhsval + "*"

                        ans+=lhsval
                    lines[j] = lines[j].split('=')[0]+"="+str(ans)+"\n"

                    

                elif '*' in rhs:
                    val = int(rhs.split('*')[1])
                    try:
                        lhsval = int(rhs.split('*')[0])
                    except:
                        lhsval = rhs.split('*')[0]
                    
                    if(type(lhsval) == int):
                        ans=lhsval
                        for i in range(val-1):
                            ans+=lhsval

                    else:
                        ans = lhsval+"+"
                        for i in range(val-2):
                            ans+=lhsval + "+"
                        ans+=lhsval        

                    lines[j] = lines[j].split('=')[0]+"="+str(ans)+"\n"


        f2 = open("optim2.py", "w")
        f2.writelines(lines)
        f2.close()            
        f.close()






