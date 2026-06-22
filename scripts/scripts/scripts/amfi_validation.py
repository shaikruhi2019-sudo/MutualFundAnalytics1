import pandas as pd

fund_master = pd.read_csv("data/raw/fundmaster.csv")
nav_history = pd.read_csv("data/raw/navhistory.csv")

print("Fund Master Columns:")
print(fund_master.columns)

print("\nNAV History Columns:")
print(nav_history.columns)