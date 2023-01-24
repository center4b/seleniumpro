import os
import time
from math import ceil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class ResponsiveTester:
    
    def __init__(self, urls):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install(), 
            options=chrome_options,
            )
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480,960,1366,1920]

    def screenshos(self,url):
        BROWSER_HEIGHT = 1360
        self.browser.get(url)
        if os.path.exists(f"{os.getcwd()}/screenshots/{url}"):
            pass
        else:
            os.mkdir(f"{os.getcwd()}/screenshots/{url}")
        for size in self.sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0,0)")
            time.sleep(3)
            scroll_size = self.browser.execute_script("return document.body.scrollHeight")
            total_sections = ceil(scroll_size / BROWSER_HEIGHT)
            for section in range(total_sections + 1):
                self.browser.execute_script(f"window.scrollTo(0,{(section) * BROWSER_HEIGHT})")
                self.browser.save_screenshot(f"screenshots/{url}/{size}x{section}.png")
                time.sleep(2)


    def start(self):
        for url in self.urls:
            self.screenshos(url)

tester = ResponsiveTester("https://naver.com")
tester.start()