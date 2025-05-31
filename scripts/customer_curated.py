# scripts/customer_curated.py
import pandas as pd
from pathlib import Path

# Define paths
input_customer_path = Path("output/customer_trusted.csv")
input_accelerometer_path = Path("output/accelerometer_trusted.csv")
output_path = Path("output/customer_curated.csv")

# Read input data
df_customer = pd.read_csv(input_customer_path)
df_accel = pd.read_csv(input_accelerometer_path)

# Join on email == user
df_merged = pd.merge(df_customer, df_accel, left_on="email", right_on="user")

# Drop 'user' column (optional)
df_curated = df_merged.drop(columns=["user"])

# Write to output
df_curated.to_csv(output_path, index=False)
print("customer_curated.csv written.")
