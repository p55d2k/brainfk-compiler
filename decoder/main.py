import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists('input.txt'):
    print("file 'input.txt' not found")
    exit()
with open('input.txt', 'r') as f:
    x = f.read()
o = ''
for i in x:
    a = ord(i)
    o += "+" * a + ".[-]"
with open('output.bf', 'w') as f:
    f.write(o)
print("Output written to 'output.bf'")