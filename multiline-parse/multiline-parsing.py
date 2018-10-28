import re
import pprint

f = open("test.txt", "r")
"""
following regex will will for patten 
abc = [
  "something",
]

\w = any char
\n= new line
\s= white spaces
.*? = makes it non-greedy. So regex will stop after first match
re.DOTALL = By default python will check patten in one line. DOTALL will convert newline to \n
"""
exp = re.compile(r'(\w+ = \[\n\s+.*?\])\n\n*', re.DOTALL)

l = exp.findall(f.read())

"""
following for loop will find all the objects with IP "20.23.201.82/32"
"""
for i in l:
    if "20.23.201.82/32" in i:
        print i
        print "\n"


f.close()


