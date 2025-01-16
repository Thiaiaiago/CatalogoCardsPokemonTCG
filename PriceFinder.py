from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def findCards():
    driver = setup()
    
    driver.implicitly_wait(5)
    
    teardown(driver)
    

def setup():
    driver = webdriver.Chrome ()
    driver.get("https://www.ligapokemon.com.br/?view=home")
    return driver

def teardown(driver):
    driver.quit()