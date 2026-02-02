from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import sys

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)  # EXE location
    return os.path.dirname(os.path.abspath(__file__))

def get_driver():
    options = Options()

    # ✅ EXPLICIT Chrome path (CHANGE if needed)
    chrome_path = r"C:\Users\ayush\AppData\Local\Google\Chrome\Application\chrome.exe"
    options.binary_location = chrome_path

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    base_dir = get_base_dir()

    # ✅ Absolute Chrome profile (works in EXE + Python)
    profile_path = os.path.join(base_dir, "chrome_profile")
    os.makedirs(profile_path, exist_ok=True)

    options.add_argument(f"--user-data-dir={profile_path}")

    service = Service()  # Selenium auto-detects driver
    driver = webdriver.Chrome(service=service, options=options)
    return driver
