from selenium.webdriver.common.keys import Keys
from config import *
from login import *

Emp_Firstname = "Mina"
Emp_Middlename = "Kumari"
Emp_Lastname = "Gupta"
Post_message = "Hi this is Supu"
Emp_Username = "Mina123"
Emp_Password = "Mina123"

# creating new PIM account
def PIM():
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]/span[1]").click()
    time.sleep(10)

    driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(5)

#entering full name
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']").send_keys(Emp_Firstname)
    time.sleep(2)

    driver.find_element(By.XPATH, "(//input[@placeholder='Middle Name'])[1]").send_keys(Emp_Middlename)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys(Emp_Lastname)
    time.sleep(2)

    empId = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    empId.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    time.sleep(2)
    empId.send_keys('9586') 
    time.sleep(2)


    
#switching label   

    driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input.oxd-switch-input--active.--label-right").click()
    time.sleep(2)        

# entering employee details
    driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys(Emp_Username)
    time.sleep(2)

    driver.find_element(By.XPATH, "(//label[normalize-space()='Enabled'])[1]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(Emp_Password)
    time.sleep(2)

    driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys(Emp_Password)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(20)


# writing a post in buzz section
def buzz():
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(12) > a:nth-child(1)").click()
    time.sleep(5)
    print("clicked buzz")

    driver.find_element(By.CLASS_NAME, "oxd-buzz-post-input").send_keys(Post_message)
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)



