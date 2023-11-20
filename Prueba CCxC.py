from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge() # o webdriver.Firefox() si usas Firefox

driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(4)
Input_user = driver.find_element(By.NAME, 'username')
Input_user.click()
Input_user.send_keys('Admin')
time.sleep(1)

password = driver.find_element(By.NAME, "password")
time.sleep(1)
password.click()
password.send_keys('admin123')

time.sleep(1)
Login = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
time.sleep(1)
Login.click()
time.sleep(8)

admin = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
time.sleep(1)
admin.click()
time.sleep(8)

add_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
time.sleep(1)
add_button.click()
time.sleep(8)   

# ADD User
# user_role = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]')
# time.sleep(1)
# user_role.click()
# user_role.click()

employee_name = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input')
employee_name.click()
employee_name.send_keys('Arnulfo pruebas')

status = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div')
status.click()
status_enable =driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]')
status_enable.click()

username_text = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')
username_text.click()
username_text.send_keys("Arnulfo Pruebas")

passw_user =driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
passw_user.click()
passw_user.send_keys("12345Admin*")

passw_confirm=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
passw_user.click()
passw_user.send_keys("12345Admin*")


save_button =driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')
save_button.click()
# resultado: es "invalid" ya que no se cumple con todos los campos requeridos. Este escenario comunmente va por cucumber para que indique la validación aunque por html se puede construir también si paso o no con los steps/units




