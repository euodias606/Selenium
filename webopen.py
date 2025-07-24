from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Create Chrome options (optional)
options = Options()
options.add_argument("--window-size=1920x1080")

# Create WebDriver instance
driver = webdriver.Chrome(options=options)

# Navigate to a website
driver.get("https://www.youtube.com/")
time.sleep(10)

# Get page title
print(driver.title)

# Close the browser
driver.quit()