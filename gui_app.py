from queue import Queue
import tkinter as tk
from tkinter import messagebox
import threading
from main_agent import run_agent

class JobAgentGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Job Auto Apply Agent")
        self.root.geometry("600x400")

        self.label = tk.Label(
            root, text="AI Job Auto Apply Agent",
            font=("Arial", 16, "bold")
        )
        self.label.pack(pady=10)

        self.log = tk.Text(root, height=12)
        self.log.pack(padx=10, pady=10)

        self.start_btn = tk.Button(
            root, text="▶ Start Agent",
            command=self.start_agent,
            bg="green", fg="white"
        )
        self.start_btn.pack(pady=5)
        self.job_queue = Queue()
        self.decision_queue = Queue()
        self.root.after(200, self.process_jobs)


    def log_msg(self, msg):
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)

    def approval_popup(self, job, score):
        msg = f"""
Job: {job['title']}
Company: {job['company']}
Platform: {job['platform']}
Match Score: {score}%
"""
        result = messagebox.askyesno("Approve Job?", msg)
        return "apply" if result else "skip"
    
    def process_jobs(self):
        if not self.job_queue.empty():
            job, score = self.job_queue.get()

            self.log_msg(f"Found: {job['title']} ({score}%)")
            decision = self.approval_popup(job, score)

            self.decision_queue.put("apply" if decision else "skip")

        self.root.after(200, self.process_jobs)

    def start_agent(self):
        self.log_msg("Agent started...")
        threading.Thread(
            target=run_agent,
            args=(self.gui_decision,),
            daemon=True
        ).start()
      


    def gui_decision(self, job, score):
        self.job_queue.put((job, score))
        return self.decision_queue.get()  # waits until popup decision

root = tk.Tk()
app = JobAgentGUI(root)
root.mainloop()
