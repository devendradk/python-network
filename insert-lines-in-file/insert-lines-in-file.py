"""
By default we can't insert a test in existing file. Below is the requirement.

Origional:
1
2
3

Modified:
1
2
1000
3

We can use readlines function and apply workaround.
readlines will read all the lines in list and we can use insert operation to insert a text.
"""

index = 0
f = open("test.txt", "r+")
i = 0

for i, x in enumerate(f):
    if "4" in x:
        position = i+1

print position
f.seek(0)
contents = f.readlines()
f.close()

value = """1000
2000
3000\n"""

contents.insert(position , value)

f = open("output.txt", "w")
contents = "".join(contents)
f.write(contents)


f.close()



