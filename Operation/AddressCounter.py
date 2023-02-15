import pandas as pd
import numpy as np
import Class.ProgramClass as Program
import Class.ExceptionClass as EX


CurrAddress = int

def FirstLine(line = list):
    global CurrAddress
    line.insert(0,hex(CurrAddress)[2:].zfill(6))
    return line

def Increment(Line = list, value = int):
    global CurrAddress
    Line.insert(0,hex(CurrAddress)[2:].zfill(6))
    CurrAddress = CurrAddress + int(str(value))
    return Line

def Type3(line = list):
    global CurrAddress
    line.insert(0,hex(CurrAddress)[2:].zfill(6))
    CurrAddress = CurrAddress + int("3",16)
    return line

def Type1(line = list):
    global CurrAddress
    line.insert(0,hex(CurrAddress)[2:].zfill(6))
    CurrAddress = CurrAddress + int("1",16)
    return line

def AddressCounter(prog = Program.Program):
    DataList = prog.DataList
    StartAddress = str(prog.HeaderList[2])
    Format3 = prog.Format3
    Format1 = prog.Format1
    df = prog.df
    global CurrAddress
    CurrAddress = int(StartAddress,16)


    for line in DataList:
        inst = str(line[1]).upper().strip()
        if str(inst) in Format3.keys():       #if key in dic.keys():
            line = Type3(line)
        elif str(inst) in Format1.keys():
            line = Type1(line)

        elif inst == "WORD":       #3
            value = 3
            line = Increment(line,value)     #3

        elif inst == "RESW":       #number * 3
            value = 3 * int(line[2])
            line = Increment(line,value)

        elif inst == "BYTE":
            if line[2][0] == 'C':        # len - 3 , add number
                value = len(line[2])-3
                line = Increment(line ,value)
            elif line[2][0] == 'X':      # len - 3 / 2
                value = int((len(line[2])-3)/2)
                line = Increment(line, value)

        elif inst == "RESB":       #+number
            value = line[2]
            line = Increment(line, value)

    pass1 = pd.DataFrame(DataList)
    #pass1.to_csv("Product/Pass1.txt", sep="\t")
    pass1.to_excel("./Product/Pass1.xlsx", encoding='utf-8', index=False)
    prog.df = pd.DataFrame(DataList)
    prog.HeaderList.insert(0,"Address")
    
    DataList = DataList[:-1]
    prog.DataList = DataList
    for i in range(0,len(DataList)):
         print(DataList[i])
    return prog