import pandas as pd
import numpy as np
import Class.ProgramClass as Program
import Class.ExceptionClass as EX

def OPcode(prog = Program.Program):
    print("welcome to OPcode")
    SymboleTable = prog.Symb
    DataList = prog.DataList
    Format3 = prog.Format3
    Format1 = prog.Format1
#________________________________________________________________________________________________________________________________________________

    for row in DataList:
        inst = str(row[2]).upper().strip()
        if inst in Format1.keys():
            row.append(Format1.get(inst))
        elif inst in Format3.keys():
            op = Format3.get(inst)
            binaryOP =  bin(int(op, 16))[2:].zfill(len(op) * 4)

#________________________________________________________________________________________________________________________________________________
# ABC
            if row[3][:1] != '#' and str(row[3]).find(',') == -1:

                if row[2] == "RSUB":     # 4c 0000
                    x = op + "0000"
                    OPfinal = x
                else:
                    address = str(SymboleTable.get(row[3]))

                    OPfinal = str(op) + address
                row.append(OPfinal)
#________________________________________________________________________________________________________________________________________________
# #ABC,x
            elif row[3][:1] == '#' and row[3].find(',') != -1:
                
                binaryOP = binaryOP[:7] + "1"
                label = str(row[3])[1:][:len(label)-3]
                address = SymboleTable.get(label)
                binaryAddress = bin(int(address, 16))[2:].zfill(len(address) * 4)
                binaryAddress = '1' + binaryAddress[1:]
                OPfinal = int(str(binaryOP) + str(binaryAddress),16)
                row.append(hex(OPfinal)[2:])
#________________________________________________________________________________________________________________________________________________
# #ABC
            elif row[3][:1] == '#' and row[3].find(',') == -1:

                binaryOP = binaryOP[:7] + "1"
                label = str(row[3])[1:]
                address = SymboleTable.get(label)
                binaryAddress = bin(int(address, 16))[2:].zfill(len(address) * 4)
                OPfinal = int(str(binaryOP) + str(binaryAddress),16)
                row.append(hex(OPfinal)[2:])
#________________________________________________________________________________________________________________________________________________
# ABC,x
            elif row[3][:1] != '#' and row[3].find(',') != -1:

                label = str(row[3])[:len(row[3])-2]
                address = SymboleTable.get(label)
               #  print(row)
               #  print(label)
               #  print(address)
                
                binaryAddress = bin(int(address, 16))[2:].zfill(len(address) * 4)
                binaryAddress ='1' + binaryAddress[1:]
               #  print(binaryAddress)
                OPfinal = int(binaryOP + binaryAddress,2)
                row.append(hex(OPfinal)[2:])
#________________________________________________________________________________________________________________________________________________

        else:
            if row[2] == "BYTE":
                if row[3][:1].upper() == 'C':
                    row.append(str(row[3])[2:-1].encode('utf-8').hex().upper())
                elif row[3][:1].upper() == 'X':
                    row.append(row[3][2:-1])
            elif row[2] == "WORD":
                a = int(str(row[3]),16)
                hexa = hex(int(row[3],16))[2:].zfill(6)
                row.append(hexa)
#________________________________________________________________________________________________________________________________________________

    prog.DataList = DataList
    pass2 = pd.DataFrame(DataList)
    pass2.replace(to_replace = np.nan, value ="*", inplace=True)
    prog.df = pass2
    #pass1.to_csv("Result/Pass1.txt", sep="\t")
    pass2.to_excel("./Result/Pass2.xlsx", encoding='utf-8', index=False)
    return prog
