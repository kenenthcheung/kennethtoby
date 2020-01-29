import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random


driver=webdriver.Chrome()
driver.get("http://servicetest.hellotoby.com:3020/zh-hk/%E8%81%98%E7%94%A8/%E5%AD%B8%E7%BF%92%E9%80%B2%E4%BF%AE/%E8%8A%AD%E8%95%BE%E8%88%9E%E7%8F%AD")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='toby-app-container-']/div[1]/div[1]/header/div/ul/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div/div/section/footer/button/span").click()
time.sleep(2)

Q=int(driver.find_element_by_xpath("//*[contains(@id, 'question-form-')]").get_attribute('id').split("-")[2])

for i in range(Q):
    if len(driver.find_elements_by_id("radio_question")) >0:
        totalR=driver.find_elements_by_id("radio_answer")
        M=len(totalR)
        if M==2:
            choices= [totalR[0],totalR[1]]
        elif M==3:
            choices = [totalR[0],totalR[1],totalR[2]]
        elif M==4:
            choices = [totalR[0],totalR[1],totalR[2],totalR[3]]
        elif M == 5:
            choices= [totalR[0],totalR[1],totalR[2],totalR[3],totalR[4]]
        elif M==6:
            choices = [totalR[0],totalR[1],totalR[2],totalR[3],totalR[4],totalR[5]]
        else:
            choices = [totalR[0],totalR[1]]
        ans = random.choice(choices)
        ans.click()
        if driver.find_elements_by_xpath("//span[contains(.,'必需填寫')]"):
            driver.find_element_by_xpath("//*[@id='radio_answer_text']").send_keys("123")
            driver.find_element_by_id("form-submit-button").click()
        elif driver.find_elements_by_xpath("//span[contains(.,'Required')]"):
            driver.find_element_by_xpath("//*[@id='radio_answer_text']").send_keys("123")
            driver.find_element_by_id("form-submit-button").click()
        else:
            driver.find_element_by_id("form-submit-button").click()

    if len(driver.find_elements_by_id("checkbox_question")) >0:
        totalC = driver.find_elements_by_id("checkbox_answer")
        MM=len(totalC)
        if MM== 2:
            choices = [totalC[0], totalC[1]]
        elif MM == 3:
            choices = [totalC[0], totalC[1],totalC[2]]
        elif MM == 4:
            choices = [totalC[0], totalC[1], totalC[2],totalC[3]]
        elif MM == 5:
            choices = [totalC[0], totalC[1], totalC[2], totalC[3],totalC[4]]
        elif MM == 6:
            choices = [totalC[0], totalC[1], totalC[2], totalC[3], totalC[4],totalC[5],totalC[6]]
        else:
            choices = [totalC[0],totalC[1]]
        ans = random.choice(choices)
        ans.click()
        if driver.find_elements_by_xpath("//span[contains(.,'必需填寫')]"):
            driver.find_element_by_xpath("//*[@id='checkbox_answer_text']").send_keys("123")
            driver.find_element_by_id("form-submit-button").click()
        elif driver.find_elements_by_xpath("//span[contains(.,'Required')]"):
            driver.find_element_by_xpath("//*[@id='checkbox_answer_text']").send_keys("123")
            driver.find_element_by_id("form-submit-button").click()
        else:
            driver.find_element_by_id("form-submit-button").click()

    if len(driver.find_elements_by_xpath("//*[@id='text_area_answer']")) >0:
        driver.find_element_by_xpath("//*[@id='text_area_answer']").send_keys("123456")
        driver.find_element_by_id("form-submit-button").click()
        time.sleep(1)

    if len(driver.find_elements_by_xpath("//input[@type='file']")) >0:
        driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/alvintang/Desktop/aaa.png")
        time.sleep(1.5)
        driver.find_element_by_id("form-submit-button").click()
    else:
        pass

if len(driver.find_elements_by_xpath("//span[contains(.,'新用戶註冊')]")) !=0:
    driver.find_element_by_xpath("//button[contains(.,'用戶登入')]").click()
    wait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='email']"))).send_keys("tester@test.com")
    wait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='password']"))).send_keys("123456")
    time.sleep(1)
    driver.find_element_by_xpath("//div[2]/div[4]/button").click()
    wait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'發佈你的需求')]"))).click()
elif len(driver.find_elements_by_xpath("//span[contains(.,'留下您的資料予專家聯繫您')]")) !=1 :
    driver.find_element_by_xpath("//button[contains(.,'發佈你的需求')]").click()
else:
    print("error")

time.sleep(3)

driver.quit()

