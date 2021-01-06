import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import subprocess

# __--Var--__#
PATH = "C:\Program Files (x86)\chromedriver.exe"
file = ("PATH TO credencials.xlsx")
df = pd.read_excel(file)
x = 0
#__--Var--__#

url_login = ("https://www.instagram.com/accounts/login")

for i in df.index:
    log = df['log'][x]
    passwd = df['passwd'][x]
    print("Using account: ", log, passwd)
    x = x + 1
    driver.implicitly_wait(5)
    driver.get(url_login)
    driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']").click()
    time.sleep(2)
    driver.find_element_by_name("username").click()
    driver.find_element_by_name("username").send_keys(log)
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").send_keys(passwd)
    driver.find_element_by_name("password").send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
    time.sleep(3)
    while True:
        driver = webdriver.Chrome(PATH)
        log = df['log'][x]
        passwd = df['passwd'][x]
        print("Using account: ", log, passwd)
        x = x + 1
        driver.implicitly_wait(5)
        driver.get(url_login)
        driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']").click()
        time.sleep(2)
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").send_keys(log)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys(passwd)
        driver.find_element_by_name("password").send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
        time.sleep(3)
        driver.close()
        if driver.find_element_by_xpath("//div[@class='JErX0']/div[@class='olLwo']") == driver.find_element_by_xpath != ("//div[@class='JErX0']/div[@class='olLwo']"):
            break()




#this still need fixing#



driver.implicitly_wait(5)
        driver.get(url_login)
        driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']").click()
        time.sleep(2)
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").send_keys(log)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys(passwd)
        driver.find_element_by_name("password").send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
        time.sleep(3)
