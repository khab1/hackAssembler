#This module contains functions to isolate destination, computation an jump 
#for c type instructions

def destination(line):
    destPresent = "=" in line
    if destPresent:
        eqlz = line.index("=")
        dest = line[0:eqlz]
        return dest
    else:
        return "null"
        
#function for extracting destination
def jump(line):
    line = line.replace("\n", "")
    jumpPresent = ";" in line
    if jumpPresent:
        jmpIndex = line.index(";")
        jump = line[jmpIndex + 1 :]
        return jump
    else:
        return "null" 
        
#function for extracting computation
def computation(line):
    line = line.replace("\n", "")
    destPresent = "=" in line
    jumpPresent = ";" in line
    eqlz = line.index("=") if destPresent else -1
    if jumpPresent:
        jmpIndex = line.index(";")
        comp = line[eqlz + 1 : jmpIndex]
    else:
        comp = line[eqlz +1 :]
    return comp