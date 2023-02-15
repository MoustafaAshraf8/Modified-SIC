import pandas as pd
import numpy as np
import Class.ProgramClass as Program
import Class.ExceptionClass as EX


def HTE(prog = Program.Program):
   print("--------------------welcome to HTE--------------------")
   #SymboleTable = prog.Symb
   DataList = prog.DataList
   # print(DataList)
   # print(DataList)
   HeaderList = prog.HeaderList
   Format3 = prog.Format3
   Format1 = prog.Format1
   inst = ["BYTE", "WORD"]
#________________________________________________________________________________________________________________________________________________
   hte = []
   #creating the H record
   # H = []
   length = hex(int(DataList[len(DataList)-2][0],16) - int(HeaderList[3],16))[2:]
   # H.insert(0,"H")
   # H.append(HeaderList[1])
   # H.append(HeaderList[3])
   # H.append(length.zfill(6))

   Hrecord = "H" + HeaderList[1] + " " + HeaderList[3] + length.zfill(6)
   
   #creating the E record
   # E = []
   # E.insert(0,"E")
   # E.insert(1,DataList[0][0])
   Erecord = "E" + DataList[0][0]
#________________________________________________________________________________________________________________________________________________

   T = []
   addressSum = 0
   i = 0
   teez = []
   Inst = True

   s=0     #second
   f=0     #first
   t = []
   # print(type(DataList[0]))
   # print(len(DataList))

   if not (DataList[0][1]):
      raise EX.MissingName()
   if len(DataList[0][1]) > 8:
      raise EX.LongerName()
   
   while s < len(DataList):
      #print(DataList[s][0])
      subt = int(DataList[s][0],16)-int(DataList[f][0],16)

      if DataList[s][3] == "RESB" and DataList[s][3] == "RESW":
            # t.insert(0,"T")
            # t.insert(1,DataList[f][0])
            # t.insert(2,int(DataList[s-1][0],16)-int(DataList[f][0],16))
            print("11111111111111111")
            x = "T"+DataList[f][0]+int(DataList[s-1][0],16)-int(DataList[f][0],16)
            x = x.join(t)
            hte.append(x)   # add string record
            t.clear()
            f=s
      
      if subt < int('00001E',16):
            #print(DataList[s][4])
            #print("1111111111111111111")
            #print(t)
            #print(DataList[s][-1])
            t.append(DataList[s][-1])
            s += 1

      elif subt >= int('00001E',16):
            t.insert(0,"T")
            t.insert(1,DataList[f][0])       #start address
            if subt > int('00001E',16):
               x = hex(int(DataList[s-1][0],16)-int(DataList[f][0],16))[2:]     #length
            else:
               x = hex(int(DataList[s][0],16)-int(DataList[f][0],16))[2:]      #length
            t.insert(2,x)
            q = "T"+ DataList[f][0] + x
            q = q.join(t)
            hte.insert(3,q)
            t.clear()
            f = s

      else:

            t.insert(0,"T")
            t.insert(1,DataList[f][0])       #start address
            s += 1

   print("__________________________________________________")
   hte.insert(0,Hrecord)   # add string
   # hte.insert(1,T)
   hte.append(Erecord)   # add string
   HTE = pd.DataFrame(hte)
   HTE.to_csv("Product/HTERecord.txt",sep='\t',index=False)
   print(HTE.to_string())

   return prog


