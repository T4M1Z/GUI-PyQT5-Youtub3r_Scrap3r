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
import win32gui
import win32con
import winxpgui
import win32api
user32 = ctypes.windll.user32
width,height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


class Channel_Scraping(QThread):
    receivedPacketSignal = pyqtSignal(dict)

    def __init__(self, ui, c_panel):
        super(Channel_Scraping, self).__init__()

        self.ui = ui
        self.c_panel_ui = c_panel 
        self.url = self.ui.url_Input.text()
        self.threads = self.ui.threads_spinBox.value()
        self.cluster = self.ui.cluster_spinBox.value() if self.ui.cluster_spinBox.isEnabled() else False
        self.yt_name = self.url.split("/")[4]
        

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
        options.add_argument("--window-position=-3500,-3500")
        options.add_argument("disable-infobars")
        options.add_argument("--kiosk")
        options.add_argument(f"--app={self.url}")

        self.driver = webdriver.Chrome(PATH, options=options)
        print(f"Canale YouTube: {self.yt_name}")
        self.driver.set_window_size(1,1)


        self.driver.get(self.url)
        time.sleep(0.5)
        # ------------------------------------------ #
        self.hwnd = 0
        self.tries = 30
        self.total_tries = 0
        while(self.hwnd==0 and self.total_tries<=self.tries):
            try:
                win32gui.EnumWindows(self.hwnd_method, None)
                self.embed_window = QtGui.QWindow.fromWinId(self.hwnd)
                self.embed_widget = QtWidgets.QWidget.createWindowContainer(self.embed_window)
                self.c_panel_ui.selenium_layout.addWidget(self.embed_widget)
                self.tries+= 1
                break
            except Exception as e:
                print(e)
                self.tries += 1
        # ------------------------------------------ #
        # self.driver.set_window_size(1,1)

        # --- * ----------------- * --- #




        # XPATH Elements location
        self.location_path = "//div[@id='details-container']//table//tbody//tr[2]//td[2]"
        self.joined_date_path = "//div[@id='right-column']//yt-formatted-string[2]//span[2]"
        self.tot_visual_path = "//div[@id='right-column']//yt-formatted-string[3]"
        self.subs_path = "//yt-formatted-string[@id='subscriber-count']"
        self.profile_img_path = "//yt-img-shadow[@id='avatar']//img"
        self.cover_img_path = "//div[@id='header']//ytd-c4-tabbed-header-renderer"
        self.social_primary = "//div[@id='primary-links']"
        self.social_secondary = "//div[@id='secondary-links']"
        self.social_path = "//div[@id='links-holder']"
        self.channel_desc_path = "//div[@id='description-container']"


    def hwnd_method(self, hwnd, ctx):
        window_title = win32gui.GetWindowText(hwnd)
        if "before you continue to youtube" in window_title.lower():
            self.hwnd = hwnd
            '''
            old_style = win32gui.GetWindowLong(hwnd, -16)
            # building the new style(old style AND NOT Maximize AND NOT Minimize)
            new_style = old_style & ~win32con.WS_MAXIMIZEBOX & ~win32con.WS_MINIMIZEBOX
            # setting new style
            win32gui.SetWindowLong(hwnd, -16, new_style)
            # updating non - client area
            win32gui.SetWindowPos(hwnd, 0, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)
            win32gui.UpdateWindow(hwnd)
            '''



    def run(self):
        # self.driver.set_window_size(1,1)

        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']//button"))).click()
            time.sleep(3)
            confirm_btn = self.driver.find_elements(By.XPATH,"//div[@class='uScs5d']//div/button")
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
            scroll = int(str(n_all_video.text).replace(",",""))//20
            scroll = 1 if scroll == 0 else scroll 
            self.driver.get(self.url)
        except Exception as e:
            try:
                print(f"errore 1 {e}")
                input = self.driver.find_element(By.XPATH, "//input[@id='search']")
                input.click()
                input.send_keys(self.yt_name)
                input.send_keys(Keys.ENTER)
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@id='video-count']")))
                n_all_video = self.driver.find_element(By.XPATH, "//span[@id='video-count']")
                scroll = int(str(n_all_video.text).replace(",","").split(" ")[0])//20
                scroll = 1 if scroll == 0 else scroll 
                time.sleep(2)
                self.driver.execute_script("window.history.go(-1)")
            except:
                print("errore 2")
                scroll = 30
                self.driver.execute_script("window.history.go(-1)")

        # Scroll the page and load more videos
        time.sleep(1)

        print(f"Questo è lo scroll: {scroll}")
        # Dict for qt signals
        video_info = {"links":[], "title":[], "visual":[], "index":[]}
        index = 0
        for n in range(scroll):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//a[@id='thumbnail']")))
                links_video = self.driver.find_elements(By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//a[@id='thumbnail']")
                title = self.driver.find_elements(By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//a[@id='video-title']")
                visual = self.driver.find_elements(By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//div[@id='metadata-line']//span[1]")
                # date = self.driver.find_elements(By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//div[@id='metadata-line']//span[2]")
                # duration = self.driver.find_elements(By.XPATH, "//div[@id='contents']//ytd-item-section-renderer//div[3]//ytd-grid-renderer//div//div[@id='overlays']//span[@id='text']")

                for l,t,v in zip(links_video,title,visual):
                    video_info["links"].append(l.get_attribute("href"))
                    video_info["title"].append(t.text)
                    video_info["visual"].append(v.text)
                    video_info["index"].append(index)
                    index+=1            
                    print(index)

                div = self.driver.find_elements(By.XPATH, "//div[@id='items']//ytd-grid-video-renderer")
                for element in div:
                    try: self.driver.execute_script("""var element = arguments[0]; 
                    element.parentNode.removeChild(element);""", element)
                    except Exception: print("err")
            except:
                print("End")

            html = self.driver.find_element(By.TAG_NAME,'html')
            html.send_keys(Keys.END)
            time.sleep(0.5)

            self.receivedPacketSignal.emit(video_info)

            print(f"scrolling [{n+1}/{scroll}] ")


        with open(f'links.txt', 'w', encoding='UTF8') as f:
            for link in video_info["links"]:
                f.writelines(link)
                f.writelines("\n")
        f.close()


        # __ INFO CHANNEL __
        self.driver.get(self.url[:-6]+"/about")

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
        try:channel_desc = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.channel_desc_path))).text
        except: channel_desc = ""

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
                if "https%3A%2F%2F" in i.get_attribute("href"):
                    a, sep, b = i.get_attribute("href").partition("https%3A%2F%2F")
                elif "http%3A%2F%2F" in i.get_attribute("href"):
                    a, sep, b = i.get_attribute("href").partition("http%3A%2F%2F")

                print(i.get_attribute("href"))
                b = b.replace(r"%2F", "/")
                b = b.replace(r"%3F", "?")
                b = b.replace(r"%3D", "=")
                socials_lst.append(b)
        except:
            print(f"[CHANNEL][SOCIAL] Error: No social?")

        self.driver.quit()

        self.receivedPacketSignal.emit({"channel_data":{"username": username,"location": location, "joined_date":joined_date,"tot_video":len(video_info["links"]), "tot_visual": tot_visual,
                        "subs":subs, "profile_img": profile_img, "cover_img":cover_img, "social": socials_lst, "channel_desc":channel_desc}})



