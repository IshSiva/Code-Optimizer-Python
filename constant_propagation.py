import re


class ConstantPropagation:

    def __init__(self, fname):
        self.fname = fname


    def run_optim(self):
        f=open(self.fname,'r')
        f2 = open("optimizer.py", "w+")

        s="([a-z]|[A-Z]|_)([a-z][A-Z][0-9])*=([0-9]|[A-Z]|[a-z]|_)+([\+\-\*\/]*([0-9]|[A-Z]|[a-z]|_))*"
        s=re.compile(s)
        assignments=[]
        l = []

        for line_i,line in enumerate(f,1):    
            if s.search(line):
                l.append(line_i)
                assignments.append(line[:-1])
        

       
        
        f.seek(0)
        line = f.readlines()
        

        for i in range(0,len(l)):
            a=assignments[i].split('=')
            lhs=a[0]
            rhs=a[1]
            
            identifier="([a-z]|[A-Z]|_)([a-z][A-Z][0-9])*=([0-9]|[A-Z]|[a-z]|_)+[\+\-\*\/\^]([0-9]|[A-Z]|[a-z]|_)"
            identifier=re.compile(identifier)
            
            
            #before=re.compile("(=|\+|\-|\*|\/|\^)+"+lhs+"[^\w]((\+|\-|\*|\/|\^)){0,1}")
            
            for j in range(l[i],line_i):
                if re.match(s,line[j]):
                    if line[j].split('=')[0]==lhs:

                        if(lhs in line[j].split('=')[1]):
                            olstr = line[j].split('=')[1]
                            nstr = olstr.replace(lhs,rhs)
                            ans = line[j].split('=')[0]+'='+nstr
                            line[j] = ans
         


                        break                

                
                z =re.match(identifier,line[j]) 
                if z:

                    if(line[j].split('=')[0] == lhs):

                        olstr = line[j].split('=')[1]
                        nstr = olstr.replace(lhs,rhs)
                        ans = z.group().split('=')[0]+'='+nstr
                        line[j] = ans
                        break

                    else:
                        olstr = line[j].split('=')[1]
                        nstr = olstr.replace(lhs,rhs)
                        ans = z.group().split('=')[0]+'='+nstr
                        line[j] = ans
                        

            


        f2.writelines(line)    
        
        
        f2.close()
        
        f.close()
