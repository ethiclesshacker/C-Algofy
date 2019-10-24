#! python3
#C Algorithm Generator

import sys
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
    if("main" in l):
        stack.append("Stop.")
        t = "Start."
    elif("int " in l):
        if(';' in l):
            t  = "Set Variables"
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
        match1 = re.findall(r'(%\w+)',l)
        match2 = re.findall(r'(,\s*)(\w+)',l)
        l = re.findall(r'".+"',l)[0]
        for i in range(len(match2)):
            l = l.replace(match1[i],match2[i][1])
        t = t + l
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
        matches = re.findall(r'(;)(.+)(;)',l)
        t = "While " + matches[0][1]
        stack.append("//Add increment/decrement here.\n"+(tab*indentCount)+"EndWhile.")
    elif("while" in l):
        t = l.replace('while',"While")
        stack.append("EndWhile.")
    elif("=" in l):
        t  = l.replace('='," <-- ")
        t  = t.replace(';',"")
    elif(l==""):
        continue
    else:
        t = l

    algo.append((tab*indentCount)+t)


algorithm = "\n".join(algo)
algorithm = algorithm.replace('('," ")
algorithm = algorithm.replace(')'," ")
algorithm = algorithm.replace('%',' MOD ')
algorithm = algorithm.replace('==',' = ')
algorithm = algorithm.replace('&&',' AND ')


for match in re.findall(r'([.]*EndIf\.\n[\s]*Else)',algorithm):
    algorithm = algorithm.replace(match,"Else")


print(text,"\n")
print(algorithm)

pyperclip.copy(algorithm)

# Example Input
"""
#include<stdio.h>
int main()
{
	int i,n,sum=0,f,s,d;
	printf("Enter number : ");
	scanf("%d", &n);
	s=n;
	while(n>0)
	{
		d=n%10;
		
		for(i=1,f=1;i<=d;i++)
		{
			f=f*i;
		}
		sum=sum+f;
		n=n/10;
	}
		if(sum==s)
		printf("%d is a peterson number", s);
		else
		printf("%d is not a peterson number", s);
}

"""
