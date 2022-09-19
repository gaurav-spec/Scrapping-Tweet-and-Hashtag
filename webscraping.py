import re
import time
import sys
from time import sleep
import pickle
import pprint
import os
import bs4
import json
import pandas as pd
import requests
import selenium
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
PATH = "C:\\Users\\sharm\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/login")
sleep(10)
print('x')
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.click()
print("Button")
username.send_keys("@gaurav30780334")
sleep(5)
user = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
user.click()
sleep(5)
userpass = driver.find_element(By.XPATH, "//input[@name='password']")
userpass.send_keys("Arun@1234")
sleep(5)
useri = driver.find_element(By.XPATH, "// span[ @class ='css-901oao css-16my406 css-1hf3ou5 r-poiln3 r-1inkyih r-rjixqe r-bcqeeo r-qvutc0'] // span[@ class ='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][normalize-space()='Log in']")
useri.click()
sleep(5)
search = driver.find_element(By.XPATH, "//input[@placeholder='Search Twitter']")
search.send_keys("Indian")
search.send_keys(Keys.ENTER)
sleep(5)
search = driver.find_element(By.XPATH, "//span[normalize-space()='Latest']")
search.click()
sleep(5)
i = 0
no_of_tweets = int(input("Please enter number of tweets to be scraped:"))
print("Number of tweets to be scraped is: " + str(no_of_tweets))
Tweets_list = []
No_list = []
Hashtag_list = []
df = pd.DataFrame(columns = ['S_No', 'Tweets', 'Hashtag'])
while (i<=no_of_tweets):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(6)
    tweet = driver.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
    print(tweet)
    hashtag = re.findall(r"[#@](\w+)", tweet)
    hashtag = str(hashtag)[1:-1]
    if hashtag=='':
        hashtag = 'No hashtag found'
    else:
        pass
    Tweets_list.append(tweet)
    Hashtag_list.append(hashtag)
    sleep(5)
    i = i + 1
    No_list.append(i)
    print("attempt no:", i)
    sleep(3)
df['S_No'] = No_list
df['Tweets'] = Tweets_list
df['Hashtag'] = Hashtag_list
df1 = pd.read_csv("C:\\Users\\sharm\\OneDrive\\Desktop\\Twetes.csv")
df2 = pd.concat([df1, df])
df2.to_csv("C:\\Users\\sharm\\OneDrive\\Desktop\\Twetes.csv", index=False)

