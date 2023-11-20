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
password.click()
password.send_keys('admin123')

time.sleep(1)
Login = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
time.sleep(1)
Login.click()
time.sleep(2)

admin = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
time.sleep(1)
admin.click()
time.sleep(3)


Button_more = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/span')
Button_more.click()

button_corp = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[1]/li')
button_corp.click()


color1  = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div')
color1.click()
color2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div')
color2.click()
color3 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div')
color3.click()
color4 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/div/div[1]')
color4.click()
color5 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[5]/div/div[2]/div/div')
color5.click()
color6 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[6]/div/div[2]/div/div')
color6.click()

publish_button =driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[3]')
publish_button.click()
# resultado: es "invalid" ya que no se cumple con todos los campos requeridos. Este escenario comunmente va por cucumber para que indique la validación aunque por html se puede construir también si paso o no con los steps/units




