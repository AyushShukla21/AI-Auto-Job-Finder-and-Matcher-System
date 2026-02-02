from resume_reader import extract_resume_text
from config import ROLES, USER_NAME
import os

def optimize_resume(job, role):
    resume_text = extract_resume_text()
    role_skills = ROLES[role]

    matched_skills = [
        skill for skill in role_skills
        if skill in job["description"].lower() and skill in resume_text
    ]

    content = f"""{USER_NAME}
Applying for: {role}

Summary:
Computer Science undergraduate with hands-on experience in
software development, machine learning, and data analysis.

Matched Skills:
"""

    for skill in matched_skills:
        content += f"• {skill.title()}\n"

    os.makedirs("optimized_resumes", exist_ok=True)
    path = f"optimized_resumes/{USER_NAME}_{role}_{job['company']}.txt"

    with open(path, "w") as f:
        f.write(content)

    return path
