import json
import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# A function to wait for a few seconds, preventing too many requests
def wait_for(sec=2):
    time.sleep(sec)

# PC search

# REMEMBER TO CHECK FOR NUMBER OF WORDS
# Get a list of words from randomlists.com
randomlists_url = "https://random-word-api.herokuapp.com/word?number=30"
response = requests.get(randomlists_url)
words_list = json.loads(response.text)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

driver = webdriver.Edge()
wait_for()
driver.get("https://rewards.bing.com")
wait_for(30)

for num, word in enumerate(words_list):
    wait = random.randint(10, 30)
    print('{0}. Searching for: {1}, {2} secs'.format(str(num + 1), word, str(wait)))
    try:
        driver.get("http://www.bing.com/")
        wait_for(3)
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.clear()
        search_box.send_keys(word)
        search_box.send_keys(Keys.ENTER)
    except Exception as e1:
        print(e1)
    wait_for(wait)

driver.close()
print("Done!")