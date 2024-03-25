from selenium.webdriver.common.keys import Keys
from config import *
from dashboard import *

comment = "Hi Supu! This is Mina"
#login 
def emp_login():
    
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(Emp_Username)
    time.sleep(2)

    #entering password
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(Emp_Password)
    time.sleep(2)

    #submit
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)
    print('employee login')

# liking and commenting on buzz 
def emp_buzz():
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(8)").click()
    time.sleep(5)
    print("clicked emp buzz")

    driver.find_element(By.ID, "heart-svg").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/button[1]/i[1]").click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Write your comment...']").send_keys(comment, Keys.ENTER)
    time.sleep(2)
    

