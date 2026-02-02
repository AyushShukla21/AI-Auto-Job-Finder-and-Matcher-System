try:
    from pypdf import PdfReader
except ModuleNotFoundError:
    print("pypdf not found. Installing...")
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    

from pypdf import PdfReader

def extract_resume_text(pdf_path="resume.pdf"):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()
