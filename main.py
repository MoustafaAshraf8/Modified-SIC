import pandas as pd
import numpy as np
import os
import glob
import Operation.Parser as parser
import Operation.AddressCounter as ad
import Class.ProgramClass as program
import Operation.SymboleTable as st
import Operation.OPcode as op
import Operation.HTErecord as hte

files = glob.glob('./Product/*')
for q in files:
   os.remove(q)
prog = parser.ParseFile("Test/in(1)_modified copy.txt")
prog = ad.AddressCounter(prog)
prog = st.SymbTable(prog)
prog = op.OPcode(prog)
prog = hte.HTE(prog)