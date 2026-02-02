import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

job = {
    "title": "Data Analyst Intern",
    "company": "Test Company",
    "platform": "Internshala"
}

msg = f"""
Job: {job['title']}
Company: {job['company']}
Platform: {job['platform']}
Match Score: 85%
"""

messagebox.askyesno("Approve Job?", msg)
