from config import ROLES
from resume_reader import extract_resume_text

def calculate_score(job_desc, role):
    resume_text = extract_resume_text()
    skills = ROLES[role]

    matched = 0
    for skill in skills:
        if skill in job_desc.lower() and skill in resume_text:
            matched += 1

    return int((matched / len(skills)) * 100)
