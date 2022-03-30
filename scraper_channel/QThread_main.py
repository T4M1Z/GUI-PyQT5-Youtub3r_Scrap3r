from PyQt5.QtCore import QThread, pyqtSignal, QObject
import time
from modules import  *
from scraper_channel.channel_scraping import Channel_Scraping

class Scraping(QObject):

    def __init__(self, ui):    
        super(Scraping, self).__init__()
        self.isRunning = False
        

    def return_channel_scraping(self, packet):
        if "loading" in packet.keys():
            print("sono il packet",packet["loading"])
        else:
            print("Sono il packet",packet)