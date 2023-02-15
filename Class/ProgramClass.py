import pandas as pd
import numpy as np

class Program:
    df = pd.DataFrame(),
    HeaderList = list,
    DataList = list,
    Symb = dict

    def __init__(self, df, D, H, f1, f3):
        self.df = df
        self.DataList = D
        self.HeaderList = H
        self.Format1 = f1
        self.Format3 = f3
        return

