#!/usr/bin/env python3
from operator import xor

lines   = []
xorrox  = []
enc     = []
key     = []
asc     = []

# read file and split by line
with open("output.txt", "rt") as inputFile:
    for line in inputFile:
        lines.append(line.strip('\n'))

# place numbers in arrays and strip extra chars
for line in lines:
    if "xorrox" in line:
        xorrox = [int(i) for i in line.replace('xorrox=[','').replace(']','').split(',')]
    elif "enc" in line:
        enc = [int(i) for i in line.replace('enc=[','').replace(']','').split(',')]

# bitxor xorrox and xorrox to key, 
# and then key and encoding to ascii
for elmt, val in enumerate(xorrox):
    k = xorrox[elmt-1] ^ xorrox[elmt]
    key.append(k)
    asc.append(chr(key[elmt] ^ enc[elmt]))

# write to file
with open("test.txt", "w") as outputFile:
    outputFile.write(f"{key=}\n")
    outputFile.write(f"{asc=}\n")
    outputFile.write(f"{xorrox=}\n")
    outputFile.write(f"{enc=}\n")
    outputFile.write(''.join(asc))