import os
import Cleaner
import Parser
import Code
from sys import argv


filepath = argv[1]

Cleaner.clean(filepath)
#this will pass the given assembly file to the cleaner
#the cleaner cleans the code and returns a file with .clean extension

cleanedCodeFile = filepath[:-3] + "clean"
f = open(cleanedCodeFile, "r")

output = filepath[:-3] + "hack"
o = open(output, "w")
for line in f:
    if line[0] == "@":
        num = int(line[1:])
        bina = bin(num)[2:]
        bina = bina.zfill(16)
        o.write(bina)
        o.write("\n")
    else:
        dest = Parser.destination(line)
        dest = Code.destination(dest)
        comp = Parser.computation(line)
        comp = Code.computation(comp)
        jump = Parser.jump(line)
        jump = Code.jump(jump)
        out = "111" + comp + dest + jump
        o.write(out)
        o.write("\n")
        
f.close()
o.close()
#os.remove(cleanedCodeFile)      #comment this line if you dont want to delete the cleaned code file