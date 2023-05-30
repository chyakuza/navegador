from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from lista import lista

driver = webdriver.Edge()
driver.get("https://www.bing.com/search?q=formula+1+ao+vivo&qs=PN&sc=8-0&cvid=59A6AA66DCDD46999CF94F4A6C8961EE&FORM=QBLH&sp=1&lq=0")
driver.implicitly_wait(20)
sleep(20)

for item in lista:
    campo_pesquisa = driver.find_element(By.XPATH,'//*[@id="sb_form"]/div/textarea')
    campo_pesquisa.click()
    campo_pesquisa.clear()
    campo_pesquisa.send_keys(item)
    campo_pesquisa.send_keys(Keys.RETURN)
    sleep(3)

driver.quit()
