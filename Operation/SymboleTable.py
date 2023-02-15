import pandas as pd
import numpy as np
import Class.ProgramClass as Program
import Class.ExceptionClass as EX



def SymbTable(prog = Program.Program):
    print("symbole table")
    DataList = prog.DataList
    SymbList = []
    SymbList.append(["Label","address"])
    for row in DataList:
        if row[1] != '*':
            if str(row[1] )== 'STL':
                print("--------------------------STL-----------------------------")
            SymbList.append([row[1], row[0]])
    pd.DataFrame(SymbList).to_excel("./Product/SymboleTable.xlsx", encoding='utf-8', index=False)
    prog.Symb = dict(SymbList)
    return prog