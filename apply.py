import time
from selenium.webdriver.common.by import By

def apply_job(driver, job, resume_path):
    driver.get(job["apply_link"])
    time.sleep(5)

    if job["platform"] == "naukri":
        try:
            apply_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]")
            apply_btn.click()
            time.sleep(3)
            print("✅ Naukri apply clicked")
        except:
            print("⚠️ Apply button not found (already applied or external)")

    else:
        print(f"ℹ️ Opened job page for {job['platform']}")
