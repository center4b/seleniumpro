import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(
        ChromeDriverManager().install(), 
        options=chrome_options,
        )

main_hashtag = "dog"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")


header = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "header"))
    )
hashtags = browser.find_elements((By.CLASS_NAME, "_add9"))

for hashtag in hashtags:
    print(hashtag.text)

time.sleep(3)
browser.quit()