from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



#variable
base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"

# config browser before it opens
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
#chrome_option.add_argument("--headless")
# chrome_option.add_argument("--incognito")

# opening browser
driver = webdriver.Chrome(chrome_option)
def browsercall():

    driver.get(base_url)
    #driver.maximize_window()
    time.sleep(5)
    print('open base url')
    time.sleep(3)


