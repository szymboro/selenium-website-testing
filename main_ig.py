import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import subprocess

# __--Var--__#
PATH = "C:\Program Files (x86)\chromedriver.exe"
df = pd.read_excel("PATH TO credencials.xlsx")
x = 0
i = 0
target_url = ("https://www.instagram.com/{TARGET NAME}")
url_login = ("https://www.instagram.com/accounts/login")
driver = webdriver.Chrome(PATH)
#__--Var--__#


for i in range(3):
        driver.get(url_login)
        driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']").click()
        log = df['log'][x]
        passwd = df['passwd'][x]
        print("Using account: ", log, passwd)
        x = x + 1
        time.sleep(10)
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").send_keys(Keys.CONTROL + "a");
        driver.find_element_by_name("username").send_keys(Keys.DELETE);
        driver.find_element_by_name("username").send_keys(log)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys(Keys.CONTROL + "a");
        driver.find_element_by_name("password").send_keys(Keys.DELETE);
        driver.find_element_by_name("password").send_keys(passwd)
        driver.find_element_by_name("password").send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
        #check_val = driver.find_elements_by_xpath("//div[@class='eiCW-']/p[@id='slfErrorAlert']")
        time.sleep(5)
        print("Login Done")
        driver.get(target_url)
        time.sleep(3)
        posts = driver.find_element_by_css_selector("li:nth-child(1)")
        print("Posts: ", posts.text)
        followers = driver.find_element_by_css_selector("li:nth-child(2)")
        print("Followers: ", followers.text)
        following = driver.find_element_by_css_selector("li:nth-child(3)")
        print("Following: ", following.text)
print (i)
