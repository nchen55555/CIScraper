# pip install selenium
# apt-get update # to update ubuntu to correctly run apt install
# apt install chromium-chromedriver
# cp /Users/nicolechen/Downloads/chromedriver

import sys
import selenium
# sys.path.insert(0,'/Users/nicolechen/Downloads/chromedriver') # this is nicole's chromedriver
# sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver') # this is kelsey's chromedriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# driver= webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome('chromedriver',options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.instagram.com/accounts/login/")
print(driver.title)

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# Log in to Instagram utilizing Campus Insights profile 

username.clear()
username.send_keys("campus_insights")

password.clear()
password.send_keys("IPOby2018Gm!")

Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))#.click()
driver.execute_script('arguments[0].click()', Login_button)

# Extract search box to input hashtag 

searchbox = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']"))) #error with timeout exception
time.sleep(10)

searchbox.clear()
hashtag = "#food"
searchbox.send_keys(hashtag)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

driver.execute_script("window.scrollBy(0,1000000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,1000000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,1000000)")
time.sleep(5)

# Acquire all blog post lings with the a attribute 

links = driver.find_elements(By.TAG_NAME, "a")

links = [link.get_attribute('href') for link in links]

profile_links = []
for link in links:
  driver.get(link)

  # checks to see if the link acquired is a valid profile 
  
  if "/p/" in link: 
    time.sleep(3)
    profile1 = driver.find_element(By.TAG_NAME, "a").get_attribute('href')
    profile = driver.find_element(By.TAG_NAME, "a").text
    profile_links.append(profile)

profile_links = {x.replace("https://www.instagram.com/", "") for x in profile_links}
usernames = []
for x in profile_links: 
  if len(x) != 0 and "https" not in x: 
    x = x.rstrip(x[-1])
    usernames.append(x)
print(usernames)

# emails = []
# for username in usernames:
#   try: 
#     filter_profiles(username)
#     if (filter_profiles(username) == True):
#       emails.append(get_user_email(username))
#   except: 
#       pass

import csv
df = pd.DataFrame(usernames,columns=["Emails"])
df.to_csv('emails.csv')


def find_email(string):
  lst = re.findall('\S+@\S+', string)
  return lst 

def get_user_email(username):
  user = InstagramUser(username, sessionid=session_id)
  if user.user_data['business_email'] != None:
    print(user.user_data['business_email'])
  elif '.com' in user.user_data['biography']:
    print(find_email(user.user_data['biography']))

# email from specific user
# get_user_email("patricia.cnr")