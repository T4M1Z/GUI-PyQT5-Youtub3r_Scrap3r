# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import win32gui
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import ctypes



# --- * Selenium Settings * --- #
PATH = os.getcwd()+"/scraper_channel/webdriver/chromedriver.exe"
options = Options()
# options.add_argument("--headless")
# options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('log-level=3')
options.add_argument("--lang=en")
options.add_argument('--disable-notifications')
options.add_argument('--mute-audio')
# options.add_argument("--kiosk")





driver = webdriver.Chrome(PATH, options=options)


driver.get("https://www.youtube.com/user/DeUanUIs/videos")

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']//button"))).click()
    time.sleep(3)
    confirm_btn = driver.find_elements(By.XPATH,"//div[@class='uScs5d']//div/button")
except Exception as e:
    print("== STEP_1 ===")

try:
    confirm_btn[0].click() # 1btn
    time.sleep(0.3)
    confirm_btn[2].click() # 2btn
    time.sleep(0.3)
    confirm_btn[4].click() # 3btn
    time.sleep(0.3)
except Exception as e:
    print("== STEP_2 ===")

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//form[@class='bBXLMd']//div/button"))).click()
except Exception as e:
    print("== STEP_2 ===")

time.sleep(2)
# Reload
link_list = []

for i in range(20):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//a[@id='thumbnail']")))
    links = driver.find_elements(By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//a[@id='thumbnail']")

    for i in links:
        link_list.append(i.get_attribute("href"))

    div = driver.find_elements(By.XPATH, "//div[@id='items']//ytd-grid-video-renderer")
    for i in div:
        try:
            driver.execute_script("""var element = arguments[0]; 
            element.parentNode.removeChild(element);""", i)
        except Exception:
            print("err")

    html = driver.find_element(By.TAG_NAME,'html')
    html.send_keys(Keys.END)
    time.sleep(0.5)
    print(len(link_list))

print(len(set(link_list)))
time.sleep(1000)