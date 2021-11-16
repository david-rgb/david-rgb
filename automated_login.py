import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common import service
from reusables import slow_typing
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import junitxml


ser = Service("C:\\Users\\adamljda\\OneDrive - Styria-IT Solutions GmbH & Co KG\\Desktop\\Python\\chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://hekaton.mojedelo.com/prijava/")



class TestHekaton:
    def test_login_open_page(self):
        assert driver.title == "Prijava - Hekaton"

    def test_login_validation_blank(self):
        blank_login = ""
        input_email = driver.find_element(By.XPATH,'//*[@id="email_login"]')
        input_password = driver.find_element(By.XPATH,'//*[@id="password"]')
        button = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/div[2]/div/div/form/button')
        input_email.clear()
        input_password.clear()
        slow_typing(input_email,blank_login)
        slow_typing(input_password,blank_login)
        button.click()
        time.sleep(2)
        valid_1 = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/div[2]/div/div/form/div[1]/div[2]/div').text
        valid_2 = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/div[2]/div/div/form/div[2]/div[2]/div').text
        time.sleep(2)
        assert valid_1 and valid_2 == 'Pravilno izpolnite polje.' and driver.title == "Prijava - Hekaton"

    def test_login_validation_wrong(self):
        wrong_email = "david_adamlje_wrong_email@outlook.com"
        wrong_pass = "asdfasdfasdfasdfasdf" 
        input_email = driver.find_element(By.XPATH,'//*[@id="email_login"]')
        input_password = driver.find_element(By.XPATH,'//*[@id="password"]')
        button = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/div[2]/div/div/form/button')
        input_email.clear()
        input_password.clear()
        slow_typing(input_email,wrong_email)
        slow_typing(input_password,wrong_pass)
        button.click()
        time.sleep(2)
        valid_err = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/div[2]/div/div/div[2]/h3').text
        time.sleep(2)
        assert  valid_err == 'Elektronski naslov ali geslo ni pravilno. Prosim poskusite ponovno.' and driver.title == "Prijava - Hekaton"
        
    def test_login_correct(self):
        email = "david.adamlje@outlook.com"
        password = "david123"
        input_email = driver.find_element(By.XPATH,'//*[@id="email_login"]')
        input_password = driver.find_element(By.XPATH,'//*[@id="password"]')
        button = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/div[2]/div/div/form/button')
        input_email.clear()
        input_password.clear()
        slow_typing(input_email,email)
        slow_typing(input_password,password)
        button.click()
        time.sleep(2)
        assert driver.title == 'MojeDelo.com - Hekaton'











