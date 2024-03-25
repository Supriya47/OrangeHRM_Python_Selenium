from config import *


def login():
    

    #entering username
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
    time.sleep(2)

    #entering password
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    time.sleep(2)

    #submit
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)
    print('admin login')



def logout():
    driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-tab").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    time.sleep(5)
    print('admin logout')

def emp_logout():
    driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    time.sleep(5)
    print("employee logout")

def browserclose():
    driver.quit()
    print('close browser')
