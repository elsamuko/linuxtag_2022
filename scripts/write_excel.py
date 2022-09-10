#!/usr/bin/env python3

import pandas as pd

table = pd.read_excel("table.xlsx")

print(table)
print("==========================")

table.at[1, 2] = "Hase"
print(table)

table.to_excel("out.xlsx")
