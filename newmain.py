from selenium import webdriver
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
#driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/checkbox')
driver.maximize_window()

main_lits = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
main_lits.click()
home_chek_box = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button')
home_chek_box.click()

file.close()