import requests
import pandas as pd
import os

schemes = {
    "HDFC": 125497,
    "SBI": 119551,
    "ICICI": 120503,
    "NIPPON": 118632,
    "AXIS": 119092,
    "KOTAK": 120841
}

os.makedirs("data/raw", exist_ok=True)

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    filename = f"data/raw/{name}.csv"
    nav_df.to_csv(filename, index=False)

    print(f"{name} saved successfully!")