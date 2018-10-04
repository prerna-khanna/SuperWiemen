import requests
import json
from urllib.request import urlopen
import pyrebase
import os
import features
import nearest_loc
import time

config = {
  "apiKey": "AIzaSyDwLt60kJLcjgLCET9KDyyj6fx2rmi1EZQ",
  "authDomain": "WieAssist-final.firebaseapp.com",
  "databaseURL": "https://WieAssist-final.firebaseio.com/",
  "storageBucket": "WieAssist-final.appspot.com",
  #"serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
st = firebase.storage()

def stream_handler(message):    
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    entry_len = len(message["path"])
    entry = message["path"]
    if(message and message['data'] != None):
        if(entry_len >1 and (entry[entry_len-1]+ entry[entry_len-2] + entry[entry_len-3] != 'mP/')):
            newpath = r"C:\Users\HP\Desktop\%s" %message["path"]
            if not os.path.exists(newpath):
                os.makedirs(newpath)
                time.sleep(2)
            st.child("uploads/air/394.jpg").download(r"C:\Users\HP\Desktop\%s\1.jpg"%message["path"])            
            features.main()
            nearest_loc.main()
my_stream = db.stream(stream_handler, stream_id="new_posts")
