# 🧠 STEDI Human Balance Analytics – Local PySpark Project

This repository implements a local version of the **STEDI Human Balance Analytics** project using **PySpark** and **Jupyter Notebooks**, simulating the data curation process originally designed for AWS Glue and Athena.

## 📘 Project Summary

STEDI has created a **Step Trainer** device and mobile app that help users improve their physical balance. The devices capture motion sensor data, which can be used to train a machine learning model that detects balance-improving movements. However, only customers who have provided **explicit consent** to share their data can be included in the model training pipeline.

This project focuses on building an **ETL pipeline** that:
- Loads raw sensor and customer data (Landing Zone)
- Filters and cleans the data based on consent (Trusted Zone)
- Aggregates relevant features to prepare for ML model input (Curated Zone)

---

## 🧱 Project Architecture

The project simulates three common data lake zones:

```
                Raw JSON Files (Landing Zone)
                      |
        ┌─────────────┴──────────────┐
        │                            │
Customer Data            Sensor Data (Accelerometer + Step Trainer)
        │                            │
        └─────► Trusted Zone (filter: shareWithResearchAsOfDate not null)
                                 |
                      Inner Join on email or serialNumber
                                 |
                      ▼
             Curated Zone (machine_learning_curated)
```

---

## 📁 Project Structure

```
stedi-etl-project/
├── data/
│   ├── customer/              # Raw customer JSON files
│   ├── accelerometer/         # Raw accelerometer JSON files
│   └── step_trainer/          # Raw step trainer JSON files
├── notebooks/
│   ├── customer_trusted.ipynb     # Create customer_trusted table
│   ├── accelerometer_trusted.ipynb # Filter accelerometer data
│   ├── customer_curated.ipynb     # Join customer + accelerometer
│   ├── step_trainer_trusted.ipynb # Filter step trainer by curated
│   └── machine_learning_curated.ipynb # Final join
├── output/
│   └── customer_trusted/      # Parquet files (simulating S3)
├── README.md
```

---

## 🧪 Technologies Used

| Tool             | Purpose                                 |
|------------------|-----------------------------------------|
| Python           | Primary language                        |
| PySpark          | Distributed data processing engine      |
| Jupyter Notebook | Interactive development and debugging   |
| Parquet          | Output format for local "S3 simulation" |

---

## ⚙️ Setup Instructions

### 1. Install Python packages

```bash
pip install pyspark jupyterlab
```

### 2. Install Java JDK (required for PySpark)

- Recommended: Java 8 or Java 11
- Download from: https://adoptium.net/en-GB/temurin/releases/

### 3. Run Jupyter Lab

```bash
cd stedi-etl-project
jupyter lab
```

Open and run the notebooks in order, starting with:
```
notebooks/customer_trusted.ipynb
```

---

## 🧩 ETL Workflow

### ✅ Step 1: Customer Trusted
- Load raw JSON
- Filter where `shareWithResearchAsOfDate` is not null
- Save as `customer_trusted` (Parquet)

### ✅ Step 2: Accelerometer Trusted
- Load accelerometer JSON
- Join with `customer_trusted` on email/user
- Save as `accelerometer_trusted`

### ✅ Step 3: Customer Curated
- Inner join `customer_trusted` and `accelerometer_trusted`
- Save as `customer_curated`

### ✅ Step 4: Step Trainer Trusted
- Load step trainer data
- Filter records based on `customer_curated` serial numbers
- Save as `step_trainer_trusted`

### ✅ Step 5: Machine Learning Curated
- Join `accelerometer_trusted` with `step_trainer_trusted` on timestamp
- Save as `machine_learning_curated`

---

## 📸 Screenshots & Results

Each stage outputs Parquet files into the `output/` folder.

Example:
```
output/customer_trusted/part-0000.snappy.parquet
```

To inspect row counts, re-load Parquet files in PySpark:
```python
df = spark.read.parquet("output/customer_trusted")
df.count()
```

---

## 📚 Reference Repositories

- [Official Udacity STEDI Project](https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises)


## 👨‍💻 Author

This project was developed by Rikki Martz as part of the Udacity Data Engineering Nanodegree program.

---

## 📝 License

This project is for educational purposes. No proprietary data is shared.
