import pandas as pd

df = pd.read_csv("data/raw/fundmaster.csv")

print("\nColumns:")
print(df.columns)

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["subcategory"].unique())

print("\nRisk Grades:")
print(df["risk_grade"].unique())