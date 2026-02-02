import time
from selenium.webdriver.common.by import By

def search_jobs(role, platform, driver):
    jobs = []

    # ---------- INTERNHALA ----------
    if platform == "internshala":
        search_url = f"https://internshala.com/internships/keywords-{role.replace(' ', '%20')}/"
        driver.get(search_url)
        time.sleep(5)

        cards = driver.find_elements(By.CLASS_NAME, "individual_internship")

        for card in cards[:5]:
            try:
                title = card.find_element(By.CLASS_NAME, "job-internship-name").text
                company = card.find_element(By.CLASS_NAME, "company-name").text
                link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

                jobs.append({
                    "title": title,
                    "company": company,
                    "description": title.lower(),
                    "apply_link": link,
                    "platform": "internshala"
                })
            except:
                continue

    # ---------- NAUKRI ----------
    elif platform == "naukri":
        search_url = (
            "https://www.naukri.com/"
            + role.replace(" ", "-").lower()
            + "-jobs"
        )

        driver.get(search_url)
        time.sleep(6)

        cards = driver.find_elements(By.CLASS_NAME, "jobTuple")

        for card in cards[:5]:  # LIMIT = 5 (SAFE)
            try:
                title = card.find_element(By.CSS_SELECTOR, "a.title").text
                company = card.find_element(By.CLASS_NAME, "subTitle").text
                link = card.find_element(By.CSS_SELECTOR, "a.title").get_attribute("href")

                jobs.append({
                    "title": title,
                    "company": company,
                    "description": title.lower(),
                    "apply_link": link,
                    "platform": "naukri"
                })
            except:
                continue

    return jobs
