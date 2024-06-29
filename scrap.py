from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

s = Service('"C:/Users/DHAN RAJ/Downloads/chromedriver_win32/chromedriver.exe"')

driver = webdriver.Chrome(service=s)
page_URL = "https://leetcode.com/problemset/all/?page="

def get_a_tags(url):
    driver.get(url)
    time.sleep(7)
    links = driver.find_elements(By.TAG_NAME, "a")
    ans = []
    for i in links:
        try:
            if "/problems/" in i.get_attribute("href"):
                ans.append(i.get_attribute("href"))
        except:
            pass
    ans = list(set(ans))
    return ans

my_ans = []
for i in range(1, 55):
    my_ans += (get_a_tags(page_URL+str(i)))

my_ans = list(set(my_ans))

with open('C:/Users/DHAN RAJ/Downloads/leetcode_problem_links.txt', 'a') as f:
    for j in my_ans:
        f.write(j+'\n')

print(len(my_ans))

driver.quit()