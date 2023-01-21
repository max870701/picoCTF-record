import sys

res = ""
with open(sys.argv[1], 'r') as f:
    line = f.readline()
    while line is not None and line != '':
        asciicode = line.split(" ")[0]
        char = chr(int(asciicode))
        res += char
        line = f.readline()
        
print(res)