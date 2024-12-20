# %% [markdown]
# **BEN Coding Interview - Premkumar Vincent**
# 
# *Testing code using Jupter*

# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time


# %%
driver = webdriver.Chrome() 
url = "http://13.209.85.69/"

def test_register(username, password, email):
    driver.get(url) 
    time.sleep(2) 
    
    # Enter data
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    email_field = driver.find_element(By.ID, "email")

    username_field.clear()
    username_field.send_keys(username)
    
    password_field.clear()
    password_field.send_keys(password)

    email_field.clear()
    email_field.send_keys(email)

    register_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Register']")
    register_button.click()
    
    # Wait for alert
    time.sleep(2)

    try:
        alert = driver.switch_to.alert
        alert_text = alert.text  # Capture alert text
        print(f"Test with username='{username}', password='{password}', email='{email}': {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print(f"Test with username='{username}', password='{password}', email='{email}': No alert dialog found")

# Test success and failure cases
# Invalid email
test_register("test123", "password", "test123") # Triggers that email is invalid

# Invalid username
test_register("test", "password123", "test123@domain.com") # username should be greater than 5 characters

# Success case

test_register("test123", "password", "test123@") # Triggers that email is invalid

driver.quit()

# %%



