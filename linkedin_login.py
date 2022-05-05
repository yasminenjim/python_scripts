from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import parameters
import time
import random
import pymongo as pymongo

#@app.route("/api/profile_url/<queryString>", methods=['POST'])
def Login():
        driver = webdriver.Chrome(parameters.chrome_driver_path)
        driver.get(parameters.linkedin_url)
        username = driver.find_element_by_name('session_key')
        username.send_keys(parameters.username)
        password = driver.find_element_by_name('session_password')
        password.send_keys(parameters.password)
        password.send_keys(Keys.RETURN)
        cookies = driver.get_cookies()
        li_at = ''    
        for i in cookies:
            if i['name'] == 'li_at':
                li_at= i['value']
                print(li_at)
Login()                   
                    
            