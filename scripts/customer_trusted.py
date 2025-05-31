import pandas as pd
import glob
import os

input_files = glob.glob("data/customer/*.json")
df = pd.concat([pd.read_json(f, lines=True) for f in input_files], ignore_index=True)
df_trusted = df[df["shareWithResearchAsOfDate"].notnull()]
os.makedirs("output", exist_ok=True)
df_trusted.to_csv("output/customer_trusted.csv", index=False)
print("customer_trusted.csv written.")
