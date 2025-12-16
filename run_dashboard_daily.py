import papermill as pm
import os
from datetime import datetime

folder = r"C:\Users\nhuet\OneDrive\Documenten\VSCode\Test"
input_path  = os.path.join(folder, "dashboard.ipynb")
output_path = os.path.join(folder, "dashboard_executed.ipynb")
final_path  = os.path.join(folder, "dashboard.ipynb")

print(f"{datetime.now():%Y-%m-%d %H:%M:%S} - Start uitvoering dashboard.ipynb")

pm.execute_notebook(input_path, output_path, progress_bar=False, log_output=True)

os.replace(output_path, final_path)

print(f"{datetime.now():%Y-%m-%d %H:%M:%S} - dashboard.ipynb succesvol ververst!")