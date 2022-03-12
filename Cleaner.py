import os

labelDict = {'R0': '0', 'R1': '1', 'R2': '2', 'R3': '3', 'R4': '4', 'R5': '5', 'R6': '6', 'R7': '7', 'R8': '8', 'R9': '9', 'R10': '10', 'R11': '11', 'R12': '12', 'R13': '13', 'R14': '14', 'R15': '15', 'SCREEN': '16384', 'KBD': '24576', 'SP': '0', 'LCL': '1', 'ARG': '2', 'THIS': '3', 'THAT': '4', 'LOOP': '4', 'WRITE': '18', 'END': '22', 'i': '16', 'sum': '17'}
#stores tha predifined symbols and store extra lables found 
   #keeps track of labels, ensuring correct address offsets
labelCounter = 0    #keeps track of labels, ensuring correct address offsets
variableDict= {' ':0}   #stores variables
variableCounter = 0     #keeps track of variables, ensuring correct address offsets

#The function cleans up comments, whitespaces and makes variables and words to numbers
def clean(filepath):
    global labelCounter
    global variableCounter
    f = open(filepath, 'r')
    o = open("cleaner.temp" , 'w')
    i = 0

    #This portion removes comments, stores labels and their positions
    for line in f:
        line = line.strip()
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        if "//" in line:
            commentIndex = line.index('//')
            line = line[0:commentIndex].strip() #removing comments
            
        if '(' in line :
            labelFound = line[1 : -1]
            labelDict[labelFound] = i  - labelCounter
            labelCounter += 1
        elif not line:
            continue    #ignore line if it is empty
        else:
            o.write(line)
            o.write('\n')
        i +=1

    o.close()
    f.close()

    f = open('cleaner.temp', 'r')
    o = open(filepath[:-3] + "clean", 'w')

    #this portion replaces variables with addresses
    for line in f:
        line = line.strip()
        if ('@' in line) and not line[1:].isnumeric():
            #the value after @ is a variable or a lable being referenced 
            variableFound = line[1:]
            if variableFound not in variableDict :
                if variableFound not in labelDict:
                    variableDict[variableFound] = 16 + variableCounter
                    o.write("@")
                    o.write(str(16 + variableCounter))
                    o.write("\n")
                    variableCounter += 1
                else:
                    o.write("@")
                    o.write(str((labelDict[variableFound])))
                    o.write("\n")
            else:
                o.write("@")
                o.write(str((variableDict[variableFound])))
                o.write('\n')
        else:
            o.write(line)
            o.write('\n')


    f.close()
    o.close()
    os.remove("cleaner.temp")
