from pymongo import MongoClient
from PyQt5.QtCore import QThread, pyqtSignal

class MongoDB(QThread): 
    receivedPacketSignal = pyqtSignal(str)
    
    def __init__(self, username, password):
        super(MongoDB, self).__init__()
        self.isRunning = False
        
        self.username = username
        self.password = password

    def stop(self):
        self.isRunning = False

    def run(self):
        self.isRunning = True
        
        while self.isRunning:
            try:
                try:
                    self.client = MongoClient(f"mongodb+srv://{self.username}:{self.password}@mongodb-main.nqvqc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                    if self.client.admin.command('ismaster')["topologyVersion"]:
                        self.receivedPacketSignal.emit("connected")
                except:
                    # Strange Error from notebook   
                    import certifi
                    ca = certifi.where()
                    self.client = MongoClient(f"mongodb+srv://{self.username}:{self.password}@mongodb-main.nqvqc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
                    if self.client.admin.command('ismaster')["topologyVersion"]:
                        self.receivedPacketSignal.emit("connected")
                    
            except Exception as e:
                self.receivedPacketSignal.emit(str(e))
