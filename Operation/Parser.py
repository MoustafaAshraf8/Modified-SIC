import pandas as pd
import numpy as np
import Class.ProgramClass as program
import Class.ExceptionClass as EX

# HeaderList = []     #program name, start, couter start address
# DataList = []       #rows data

Format3 = dict({
    "ADD":"18",
    "AND":"40",
    "COMP":"28",
    "DIV":"24",
    "J":"3C",
    "JEQ":"30",
    "JGT":"34",
    "JLT":"38",
    "JSUB":"48",
    "LDA":"00",
    "LDCH":"50",
    "LDL":"08",
    "LDX":"04",
    "MUL":"20",
    "OR":"44",
    "RD":"D8",
    "RSUB":"4C",
    "STA":"0C",
    "STCH":"54",
    "STL":"14",
    "STSW":"E8",
    "STX":"10",
    "SUB":"1C",
    "TD":"E0",
    "TIX":"2C",
    "WD":"DC",
})
Format1 = dict({
    "FIX":"C4",
    "FLOAT":"C0",
    "HIO":"F4",
    "NORM":"C8",
    "SIO":"F0",
    "TIO":"F8"
})

def CreateDefault(df):
    df.to_excel("./Result/1-default.xlsx", encoding='utf-8', index=False)

def CreateIntermediate(df):
    df.to_excel("./Result/2-intermediate.xlsx", encoding='utf-8', index=False)
    
def DataToList(df = pd.DataFrame):
    DataList = df.values.tolist()
    return DataList
    
def GetHeader(df):
    HeaderList = []
    for col in df.columns:
        HeaderList.append(col)
    return HeaderList
    


def ParseFile(FilePath):
    try:
        df = pd.read_csv(FilePath, delimiter="\t")
        global Format1
        global Format3
        CreateDefault(df)
        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[3], axis=1, inplace=True)

        rows = []
        for i in (0, len(df)-1):
            if str(df.iloc[i,0]) == '.' or pd.isnull(df.iloc[i,1]):
                continue
            else:
                rows.append(df.iloc[i])

        df.replace(to_replace = np.nan, value ="*", inplace=True)
        
        DataList = DataToList(df)
        HeaderList = GetHeader(df)
        
        
        df.to_excel("Result/intermediate.xlsx", encoding='utf-8', index=False)
        x = program.Program(df, DataList, HeaderList, Format1, Format3)
        return x
    except EX.LessColumns:
        print('here')
        EX.LessColumns()
    finally:
        print("_____________________________________________________________________")
