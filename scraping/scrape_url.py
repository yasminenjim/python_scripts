from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import parameters
import time
import random
import pymongo as pymongo


def insert(item,keyword):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["mydatabase"]
	profile_urls = mydb["profile_urls"]

	url = { "url": item ,"keyword":keyword}

	x = profile_urls.insert_one(url)

#@app.route("/api/profile_url/<queryString>", methods=['POST'])
def get(queryString):
        linkedin_web_elements = []
        driver = webdriver.Chrome(parameters.chrome_driver_path)
        driver.get(parameters.google_url)
        search_query = driver.find_element_by_name('q')
        search_query.send_keys(parameters.search_query_1 + queryString + parameters.search_query_2+parameters.country)
        #time.sleep(random.randint(10, 20))
        search_query.send_keys(Keys.RETURN)
    

##all pages
        last_page_content='afficher les résultats les plus pertinents'
        last_page = False 

        while not last_page:

            linkedin_web_elements=driver.find_elements_by_xpath("//div[contains(@class, 'g')]//a")
            for item in linkedin_web_elements:
                if('google' not in item.get_attribute("href")):
                    profile=item.get_attribute("href")
                    x = profile.find("/")
                    y = profile.find(".")
                    profile=profile.replace(profile[x+2:y],"www")
                    print(profile)
                    insert(profile,queryString)
                    
                    
                    
                    
            ####### all google pages
            next_page=''
            next_page = driver.find_element_by_xpath("//a[@id='pnnext']").get_attribute("href")
            
            driver.get(next_page)
            
            elem = driver.find_element_by_xpath("//*")
            source_code = elem.get_attribute("outerHTML")
        
            #to iterate through all google result pages
            #last_page=last_page_content in source_code
            
            # to force it just to parse the first page ( to delete it later and uncomment the previous line )
            #last_page=True
            
              # END ####### all google pages
            
        
            time.sleep(random.randint(10, 20))
            #driver.quit()
            #linkedin_urls = linkedin_urls[:4]
           
        print(linkedin_urls)
        
        return linkedin_urls

#get('nodejs')