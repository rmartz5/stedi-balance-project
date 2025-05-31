import pandas as pd
import glob
import os

input_files = glob.glob("data/accelerometer/*.json")
df = pd.concat([pd.read_json(f, lines=True) for f in input_files], ignore_index=True)
df_trusted = df[df["user"].notnull()]
os.makedirs("output", exist_ok=True)
df_trusted.to_csv("output/accelerometer_trusted.csv", index=False)
print("accelerometer_trusted.csv written.")
