import pandas as pd
import glob
import os

input_files = glob.glob("data/step_trainer/*.json")
df = pd.concat([pd.read_json(f, lines=True) for f in input_files], ignore_index=True)
df_trusted = df[df["sensorReadingTime"].notnull()]
os.makedirs("output", exist_ok=True)
df_trusted.to_csv("output/step_trainer_trusted.csv", index=False)
print("step_trainer_trusted.csv written.")
