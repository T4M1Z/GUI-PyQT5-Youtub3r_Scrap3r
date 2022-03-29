from pymongo import MongoClient
import json
import os
import csv
import time
import sys
import natsort 

class MongoDB: 
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def test_connection(self):
        try:
            try:
                self.client = MongoClient(f"mongodb+srv://{self.username}:{self.password}@mongodb-main.nqvqc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                if self.client.admin.command('ismaster')["topologyVersion"]:
                    return "connected"
            except:
                # Strange Error from notebook   
                import certifi
                ca = certifi.where()
                self.client = MongoClient(f"mongodb+srv://{self.username}:{self.password}@mongodb-main.nqvqc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
                if self.client.admin.command('ismaster')["topologyVersion"]:
                    return "connected"
                
        except Exception as e:
            return e
