import pandas as pd
import numpy as np
import os
import glob
import Parser as parser
import AddressCounter as ad
import Class.ProgramClass as program
import SymboleTable as st
import OPcode as op
import HTErecord as hte

files = glob.glob('./Product/*')
for q in files:
   os.remove(q)
prog = parser.ParseFile("Test/in(1)_modified copy.txt")
prog = ad.AddressCounter(prog)
prog = st.SymbTable(prog)
prog = op.OPcode(prog)
prog = hte.HTE(prog)