# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class channel_scraping:
    def __init__(self):
        
        print(os.getcwd())
        PATH = os.getcwd()+"/scraper_channel/webdriver/chromedriver.exe"
        options = Options() 

        # options.add_argument("--headless")
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('log-level=3')
        options.add_argument("--lang=en")
        options.add_argument('--disable-notifications')
        options.add_argument('--mute-audio')
        self.driver = webdriver.Chrome(PATH, options=options)

        # PAth
        self.location_path = "//div[@id='details-container']//table//tbody//tr[2]//td[2]"
        self.joined_date_path = "//div[@id='right-column']//yt-formatted-string[2]//span[2]"
        self.tot_visual_path = "//div[@id='right-column']//yt-formatted-string[3]"
        self.subs_path = "//yt-formatted-string[@id='subscriber-count']"
        self.profile_img_path = "//yt-img-shadow[@id='avatar']//img"
        self.cover_img_path = "//div[@id='header']//ytd-c4-tabbed-header-renderer"
        self.social_path = "//div[@id='links-holder']"



    def Youtube_Channel(self, url, ch_name):
        print(f"Canale YouTube: {ch_name}")
        self.driver.get(url)


        try: 
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']//button"))).click()
            time.sleep(3)
            confirm_btn = self.driver.find_elements(By.XPATH,"//div[@class='uScs5d']//div/button")
        except Exception as e:
            print("== STEP_1 ===")
        
        try: 
            confirm_btn[0].click() # 1btn
            time.sleep(1)
            confirm_btn[2].click() # 2btn
            time.sleep(1)
            confirm_btn[4].click() # 3btn
            time.sleep(1)
        except Exception as e:
            print("== STEP_2 ===")

        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//form[@class='bBXLMd']//div/button"))).click()
        except Exception as e:
            print("== STEP_2 ===")

        username = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//ytd-channel-name[@id='channel-name']"))).text
        # 1scroll = 30video
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='primary-items']//yt-dropdown-menu//tp-yt-paper-menu-button//div"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='contentWrapper']//div//tp-yt-paper-listbox//a[1]//tp-yt-paper-item//tp-yt-paper-item-body"))).click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='play-button']//ytd-button-renderer//a")))
            link_all_video = self.driver.find_element(By.XPATH, "//div[@id='play-button']//ytd-button-renderer//a")
            self.driver.get(link_all_video.get_attribute("href"))
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='publisher-container']//div//yt-formatted-string//span[3]")))
            n_all_video = self.driver.find_element(By.XPATH, "//div[@id='publisher-container']//div//yt-formatted-string//span[3]")
            print("Numero video: ",n_all_video.text)
            scroll = int(str(n_all_video.text).replace(",",""))//23
            self.driver.get(url)
        except Exception as e:
            try:
                print(f"errore 1 {e}")
                input = self.driver.find_element(By.XPATH, "//input[@id='search']")
                input.click()
                input.send_keys(ch_name)
                input.send_keys(Keys.ENTER)
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@id='video-count']")))
                n_all_video = self.driver.find_element(By.XPATH, "//span[@id='video-count']")
                scroll = int(str(n_all_video.text).replace(",","").split(" ")[0])//27
                time.sleep(2)
                self.driver.execute_script("window.history.go(-1)")
            except:
                print("errore 2")
                scroll = 30
                self.driver.execute_script("window.history.go(-1)")


        # Scroll the page and load more videos
        time.sleep(1)
        for i in range(scroll):
            html = self.driver.find_element(By.TAG_NAME,'html')
            html.send_keys(Keys.END)
            print(f"scrolling [{i+1}/{scroll}]")
            time.sleep(0.5)


        # Reload
        links = self.driver.find_elements(By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//a[@id='thumbnail']")

        #codice va lento su canale con molti iscritti
        links = [i.get_attribute("href") for i in links]


        with open(f'links.txt', 'w', encoding='UTF8') as f:
            for link in links:
                f.writelines(link)
                f.writelines("\n")
        f.close()
        

        # __ INFO CHANNEL __
        self.driver.get(url[:-6]+"/about")
        
        try:location = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.location_path ))).text
        except: location = ""
        try:joined_date = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.joined_date_path))).text
        except: joined_date = ""
        try:tot_visual = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.tot_visual_path))).text
        except: tot_visual = ""
        try:subs = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.subs_path))).text
        except: subs = ""
        try:profile_img = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.profile_img_path))).get_attribute("src")
        except: profile_img = ""
        
        # Cover img
        try:
            cover_img = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.cover_img_path))).get_attribute("style")
            a, sep, b = str(cover_img).partition(".com")
            b = b[1:].split("\\")[0]
            cover_img = "https://yt3.ggpht.com"+b
        except Exception as e: print(f"[CHANNEL][COVER IMG] Error: {e}")
        
        
        # Links social
        socials_lst = []         
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.social_path)))
            socials = self.driver.find_elements(By.XPATH, self.social_path + "//a")
            for i in socials:
                a, sep, b = i.get_attribute("href").partition("https%3A%2F%2F")
                b = b.replace(r"%2F", "/")
                b = b.replace(r"%3F", "?")
                b = b.replace(r"%3D", "=")
                socials_lst.append(b)
        except: print(f"[CHANNEL][SOCIAL] Error: No social?")

        print(ch_name)
        print(location)
        print(joined_date)
        print(tot_visual)
        print(subs)
        print(profile_img)
        print(cover_img)

        
        self.driver.quit()
        print(f"Numero di video trovati: {len(links)}")

        print({"username": username,"location": location, "joined_date":joined_date,"tot_video":len(links), "tot_visual": tot_visual, 
                        "subs":subs, "profile_img": profile_img, "cover_img":cover_img, "social": socials_lst})
        return {"username": username,"location": location, "joined_date":joined_date,"tot_video":len(links), "tot_visual": tot_visual, 
                        "subs":subs, "profile_img": profile_img, "cover_img":cover_img, "social": socials_lst}
    
