from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class GoogleKeywordScreenshooter():
    
    def __init__(self, keyword, screenshots_dir):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install(), 
            options=chrome_options,
            )
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir
        
        
    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element(By.CLASS_NAME, "gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        try:
            shitty_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(By.CLASS_NAME, "kvH3mc"))
            self.browser.execute_script(
                """
            const shitty = argument[0];
            shitty.parentElement.removeChild(shitty)
            """, 
                shitty_element,
            )
        except Exception:
            pass
        search_results = self.browser.find_elements(By.CLASS_NAME, "kvH3mc")
        for index, search_result in enumerate(search_results):
            class_name = search_result.get_attribute("class")
            search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}x{index}.png")
            
    def finish(self):
        self.browser.quit()

domain_competitors = GoogleKeywordScreenshooter("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenshooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()
