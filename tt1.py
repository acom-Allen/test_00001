
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Show current work place
#print("This is your work place : ", os.getcwd())

# Ignore Certificate
driver_options = webdriver.ChromeOptions()
driver_options.add_argument('ignore-certificate-errors')
driver_options.add_argument('--headless')
driver_options.add_argument('--disable-gpu')

# Open Webdriver
driver = webdriver.Chrome(options=driver_options)
driver.get('https://192.168.0.14/')    # This is ACOM HP-Printer Website IP

time.sleep(1)

# Enter Tools
tool_button = driver.find_element(By.ID, "top-cat-Tools")
tool_button.click()

time.sleep(2)

# PowerCycle 
menu_button = driver.find_element(By.XPATH, '//*[@id="CatTools"]/div[6]/div[1]')
menu_button.click()
menu_power_button = driver.find_element(By.ID, "nav-pgPowerCycle")
menu_power_button.click()
#<input type="button" class="gui-cmd-bar-btn gui-cmd-bar-btn-power_cycle gui-action-btn" value="電源循環">

time.sleep(1)

power_button = driver.find_element(By.CLASS_NAME, "gui-action-btn")
power_button.click()

# Jump-window is based on Chrome browers
#alert_object = driver.switch_to
#print(alert_object)
time.sleep(1)

# Click YES button to restart HP-Printer
#/html/body/div[4]/div[2]/button[1]
yes_button = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/button[1]')
yes_button.click()

time.sleep(2)

print("This is your work place : ", os.getcwd())

driver.quit()

print("Success")

