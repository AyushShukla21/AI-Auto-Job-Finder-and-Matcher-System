from browser import get_driver
from search_jobs import search_jobs
from matcher import calculate_score
from resume_optimizer import optimize_resume
from apply import apply_job
from tracker import save_job
from config import ROLES, PLATFORMS, MIN_MATCH_SCORE

def run_agent(gui_callback=None):
    driver = get_driver()

    for role in ROLES:
        for platform in PLATFORMS:
            print(f"🔍 Searching jobs for {role} on {platform}")
            jobs = search_jobs(role, platform)

            for job in jobs:
                print(f"📄 Job found: {job['title']} | Company: {job['company']}")

                score = calculate_score(job["description"], role)

                # --- GUI MODE ---
                if gui_callback:
                    decision = gui_callback(job, score)
                    if decision != "apply":
                        continue

                # --- NON GUI MODE ---
                else:
                    if score < MIN_MATCH_SCORE:
                        continue

                # ✅ SAFE: resume_path always defined before use
                resume_path = optimize_resume(job, role)
                apply_job(driver, job, resume_path)
                save_job(job, role)

    print("✅ Agent run completed.")
