import json
import time
import logging
import random

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# A function to wait for a few seconds, preventing too many requests
def wait_for(sec=2):
    time.sleep(sec)

# Mobile search

# Get a list of 20 words from randomlists.com
randomlists_url = "https://random-word-api.herokuapp.com/word?number=20"
response = requests.get(randomlists_url)
words_list = json.loads(response.text)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

# Define mobile emulation options
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Android 6.0.1; Mobile; rv:63.0) Gecko/63.0 Firefox/63.0"
}

# Set up Microsoft Edge options with mobile emulation
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("mobileEmulation", mobile_emulation)

# Create Edge WebDriver instance with options
driver = webdriver.Edge(options=edge_options)

# Set window size (optional)
driver.set_window_size(360, 640)

# Navigate to a website
driver.get("https://rewards.bing.com")
wait_for(10)

# Perform mobile search actions
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
        logging.error('An error occurred: %s', e1)
    wait_for(wait)

# Close the browser
driver.quit()
print("Done!")