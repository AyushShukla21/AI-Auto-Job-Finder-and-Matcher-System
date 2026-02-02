from browser import get_driver

driver = get_driver()
driver.get("https://www.google.com")
input("Press Enter to close...")
driver.quit()
