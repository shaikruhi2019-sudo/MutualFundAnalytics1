import os
import pandas as pd

folder = "data/raw"

csv_files = [f for f in os.listdir(folder) if f.endswith(".csv")]

print(f"\nTotal CSV files found: {len(csv_files)}\n")

for file in csv_files:
    print("=" * 80)
    print(f"Dataset: {file}")

    try:
        df = pd.read_csv(os.path.join(folder, file))

        print(f"\nShape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")

    print("=" * 80)