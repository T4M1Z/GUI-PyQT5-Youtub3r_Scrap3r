from ast import arg
import pymongo
from pymongo import MongoClient
from PyQt5.QtCore import QThread, pyqtSignal
from global_variables import GlobalVariables
import threading
import time
import datetime
from bson.objectid import ObjectId


class DBConnection(QThread): 
    receivedPacketSignal = pyqtSignal(str,list)
    
    def __init__(self, string, mode):
        super(DBConnection, self).__init__()
        self.isRunning = False
        self.string = string
        self.mode = mode
        

    def stop(self):
        self.isRunning = False

    def run(self):
        self.isRunning = True
        print("is running")
        while self.isRunning:
            try:
                try:
                    import certifi
                    ca = certifi.where()
                    self.client = MongoClient(self.string, tlsCAFile=ca)
                    if self.client.admin.command('ismaster')["topologyVersion"]:
                        pass
                except:
                    self.client = MongoClient(self.string)
                    if self.client.admin.command('ismaster')["topologyVersion"]:
                        pass

                if self.mode == "insert_data_channel":
                    print("sto inserendo i dati nel db")
                    self.insert_data_channel()
                    break

                elif self.mode == "select_channel":
                    print(f"Queto è l'id che andrò a selezionare {GlobalVariables.SELECTED_DATA_CHANNEL}")
                    self.request_data_channel()
                    break
                
                if self.mode == "remove_channel":
                    print(f"sto per rimuovere questo channel {GlobalVariables.SELECTED_DATA_CHANNEL}")
                    self.remove_channel()
                    break

                else:
                    self.history_channel_query()
                    break

            except Exception as e:
                self.receivedPacketSignal.emit("error " + str(e), [])
                break





    def history_channel_query(self, val = None):
        db = self.client['channels_analytics']
        collection = db['data_channel']

        if "channels_analytics" not in self.client.list_database_names():
            print("nessun dato ancora registrato")
        else:
            q = [data for data in collection.find({},{"_id":1,"username":1,"profile_img":1,"timestamp":1}).sort('timestamp',pymongo.DESCENDING)] 
            # q = [i for i in collection.find().sort({"timestamp": -1})] 
            if val:
                self.receivedPacketSignal.emit(val,q)
            else:
                self.receivedPacketSignal.emit(self.mode,q)
            

    def insert_data_channel(self):
        db = self.client['channels_analytics']
        collection = db['data_channel']
        for k,v in GlobalVariables.CHANNEL_DATA.items():
            print(k, type(v))

        collection.insert_one(GlobalVariables.CHANNEL_DATA)
        self.receivedPacketSignal.emit(self.mode,[])


    def request_data_channel(self):
        db = self.client['channels_analytics']
        collection = db['data_channel']

        q = [data for data in collection.find({"_id": ObjectId(GlobalVariables.SELECTED_DATA_CHANNEL)})]

        self.receivedPacketSignal.emit(self.mode,q) 

    def remove_channel(self):
        db = self.client['channels_analytics']
        collection = db['data_channel']

        collection.delete_one( {"_id": ObjectId(GlobalVariables.SELECTED_DATA_CHANNEL)})
        q = [data for data in collection.find({},{"_id":1,"username":1,"profile_img":1,"timestamp":1}).sort('timestamp',pymongo.DESCENDING)] 

        self.receivedPacketSignal.emit(self.mode,q) 