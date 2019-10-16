#! python3
#C Algorithm Generator

import sys
import os
import re
import pyperclip

if(len(sys.argv)<2):
    text = pyperclip.paste()
else:
    fileName = sys.argv[1]
    text = ""

lines = text.split('\n')
indentCount = -1
tab = "\t"
c = 0

algo = []
stack = []

for l in lines:
    lines[c] = l.strip()
    c = c + 1

for l in lines:
    t = ''
    if("void" in l):
        stack.append("Stop.")
        t = "Start."
    elif("int " in l):
        if(';' in l):
            t  = "Set Variables"
    elif(" = " in l):
            t  = l.replace('=',"<--")
            t  = t.replace(';',"")
    elif(l =='{'):
        indentCount = indentCount + 1
        continue
    elif(l == '}'):
        indentCount = indentCount - 1
        t = stack[-1]
        stack.pop()    
    elif("scanf" in l):
        t = "Read "
        var = re.findall(r'&([\w\d]*)',l)
        t = t  + ', '.join(var)
    elif("gets" in l):
        t = "Read "
        var = re.findall(r'\(([\w\d]*)\)',l)
        t = t  + ', '.join(var)
    elif("printf" in l):
        t = "Print "
        var = re.findall(r',(.+)\)',l)
        l = ' '.join(var)
        var = re.findall(r'(\w+)',l)
        t = t + ', '.join(var)
    elif("puts" in l):
        t = "Print "
        var = re.findall(r'\(([\w\d]*)\)',l)
        t = t  + ', '.join(var)
    elif("else" in l):
        t = l.replace('if',"If")
        t = t.replace('else',"Else")
        stack.append("EndIf.")
    elif("if(" in l):
        t = l.replace('if',"If")
        stack.append("EndIf.")
    elif("for" in l):
        t = "While..."
        stack.append("EndWhile.")
    elif("while" in l):
        t = l.replace('while',"While")
        stack.append("EndWhile.")
    else:
        t = l

    algo.append((tab*indentCount)+t)


algorithm = "\n".join(algo)
algorithm = algorithm.replace('('," ")
algorithm = algorithm.replace(')'," ")
algorithm = algorithm.replace('%',' MOD ')
algorithm = algorithm.replace('==',' = ')
algorithm = algorithm.replace('&&',' AND ')
algorithm = algorithm.replace("EndIf.\nElse","Else")


print(text,"\n")
print(algorithm)

#pyperclip.copy(algorithm)

# Example Input
"""
void main()
{
    int a = 5;
    a = 6;
    b = a % 3;
    if(a%5 == 0)
    {
        printf("");
        printf("");
        while(a<4)
        {
            printf("");
            scanf("");
        }
    }
    else if(a == 0)
    {
        scanf("%d",&length,&str1,&c2);
    }
    else
    {
        printf("Hello my name is %d",name, class)
    }
    scanf("");
}

"""
