# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d94f5#problem

def switch(s):  
    i=0
    n=''
    while i+3<=len(s):
        if int(s[i+1]) == (int(s[i])+1):
            n+=str(int(s[i])+2)
            s=n+s[i+2:]
        else:
            n+=s[i]
        i+=1
    return s

  ### loops the first function until there are no substitutions left
def repeater(s):       
    a=switch(s)
    b=switch(a)
    while a!=b:
        a=b
        b=switch(a)
    return b
print(switch(s))
print(repeater(s))