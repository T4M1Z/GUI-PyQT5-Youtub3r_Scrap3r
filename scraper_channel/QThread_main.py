from PyQt5.QtCore import QThread, pyqtSignal
import time
from modules import  *
from scraper_channel.channel_scraping import channel_scraping


class Scraping(QThread):
    receivedPacketSignal = pyqtSignal(dict)

    def __init__(self, url, threads, cluster):    
        super(Scraping, self).__init__()
        self.isRunning = False

        self.url = url
        self.threads = threads
        self.cluster = cluster
        self.yt_name = url.split("/")[4] 

    def stop(self):
        self.isRunning = False

    def run(self):
        self.isRunning = True
        self.receivedPacketSignal.emit({"message":"Is starting"})
        
        while self.isRunning:
            self.start_channel_scraping()
            time.sleep(1)
            print("end")
            break


    def start_channel_scraping(self):
        # ---------------------- #
        # Start Channel Scraping
        # _______________________#
    
        scrap = channel_scraping()
        self.channel_info_box = scrap.Youtube_Channel(self.url, self.yt_name)
        self.yt_name = self.channel_info_box["username"]
        self.receivedPacketSignal.emit({"channel_data":self.channel_info_box})
        
