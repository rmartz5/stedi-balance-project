# scripts/pipeline_runner.py
import subprocess

scripts = [
    "scripts/customer_trusted.py",
    "scripts/accelerometer_trusted.py",
    "scripts/step_trainer_trusted.py",
    "scripts/customer_curated.py",
    "scripts/machine_learning_curated.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(["python", script], check=True)
