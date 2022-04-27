from pymongo import MongoClient
from PyQt5.QtCore import QThread, pyqtSignal

import time
import datetime

class DBConnection(QThread): 
    receivedPacketSignal = pyqtSignal(str,list)
    
    def __init__(self, string, mode):
        super(DBConnection, self).__init__()
        self.isRunning = False
        self.string = string
        self.mode = mode
        "mongodb+srv://root:root@mongodb-main.nqvqc.mongodb.net/test?authSource=admin&replicaSet=atlas-w2onn2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"

    def stop(self):
        self.isRunning = False

    def run(self):
        self.isRunning = True
        print("is running")
        while self.isRunning:
            try:
                try:
                    self.client = MongoClient(self.string)
                    if self.client.admin.command('ismaster')["topologyVersion"]:
                        self.history_channel_query()

                    break
                
                except:
                    # Strange Error from notebook   
                    import certifi
                    ca = certifi.where()
                    self.client = MongoClient(self.string, tlsCAFile=ca)
                    if self.client.admin.command('ismaster')["topologyVersion"]:
                        self.history_channel_query()
                        self.receivedPacketSignal.emit("connected",[])
                    break
                    
            except Exception as e:
                self.receivedPacketSignal.emit("error " + str(e), [])
                break

    def history_channel_query(self):
        db = self.client['channels_analytics']
        collection = db['data_channel']

        if "channels_analytics" not in self.client.list_database_names():
            print("nessun dato ancora registrato")
            # post = {"author": "Mike",
            #     "text": "My first blog post!",
            #     "tags": ["mongodb", "python", "pymongo"],
            #     "date": datetime.datetime.utcnow()}
            
            # post_id = collection.insert_one(post).inserted_id
        else:
            q = [i for i in collection.find()] 
            self.receivedPacketSignal.emit(self.mode,q)
            

