# scripts/machine_learning_curated.py
import pandas as pd

# Load the trusted datasets
df_step = pd.read_csv("output/step_trainer_trusted.csv")
df_customer = pd.read_csv("output/customer_curated.csv")

# Convert customer 'timestamp' to datetime, then to milliseconds since epoch
df_customer["timestamp"] = pd.to_datetime(df_customer["timestamp"])
df_customer["timestamp_millis"] = (df_customer["timestamp"].astype('int64') // 10**6)

# Optional: round both times to the nearest second or floor/truncate to avoid mismatches
# e.g., rounding for merge alignment (if appropriate to data)
df_customer["timestamp_millis_rounded"] = df_customer["timestamp_millis"] // 1000
df_step["sensorReadingTime_rounded"] = df_step["sensorReadingTime"] // 1000

# Merge on rounded values
df_merged = pd.merge(
    df_step,
    df_customer,
    left_on="sensorReadingTime_rounded",
    right_on="timestamp_millis_rounded",
    how="inner"
)

# Select relevant columns for output
df_curated = df_merged[["email", "sensorReadingTime", "distanceFromObject"]]

# Save curated dataset
df_curated.to_csv("output/machine_learning_curated.csv", index=False)
print("machine_learning_curated.csv written.")
