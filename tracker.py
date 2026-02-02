import pandas as pd
from datetime import date
import os
import sys

def save_job(job, role):
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)  # EXE location
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(base_dir, "jobs_applied.xlsx")

    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(
            columns=["Date", "Role", "Company", "Platform", "Status"]
        )

    df.loc[len(df)] = [
        date.today(),
        role,
        job["company"],
        job["platform"],
        "Applied"
    ]

    df.to_excel(file_path, index=False)
