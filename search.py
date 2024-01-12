import json
import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# A function to wait for a few seconds, preventing too many requests
def wait_for(sec=2):
    time.sleep(sec)


# PC search

# Get a list of 30 words from randomlists.com
randomlists_url = "https://www.randomlists.com/data/words.json"
response = requests.get(randomlists_url)
words_list = random.sample(json.loads(response.text)['data'], 30)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

driver = webdriver.Edge()
wait_for(5)

for num, word in enumerate(words_list):
    print('{0}. Searching for: {1}'.format(str(num + 1), word))
    try:
        driver.get("http://www.bing.com/")
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.clear()
        search_box.send_keys(word)
        search_box.send_keys(Keys.ENTER)
    except Exception as e1:
        print(e1)
    wait_for(7.5)

driver.close()


# Mobile search

# Get a list of 20 words from randomlists.com
randomlists_url = "https://www.randomlists.com/data/words.json"
response = requests.get(randomlists_url)
words_list = random.sample(json.loads(response.text)['data'], 20)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Android 6.0.1; Mobile; rv:63.0) Gecko/63.0 Firefox/63.0")

options = Options()
options.profile = profile

driver = webdriver.Firefox(options=options)
driver.set_window_size(360,640)
wait_for(5)

for num, word in enumerate(words_list):
    print('{0}. Searching for: {1}'.format(str(num + 1), word))
    try:
        driver.get("http://www.bing.com/")
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.clear()
        search_box.send_keys(word)
        search_box.send_keys(Keys.ENTER)
    except Exception as e1:
        print(e1)
    wait_for(7.5)

driver.close()

