import pyrebase
from geopy.geocoders import Nominatim
import csv
from math import radians, cos, sin, asin, sqrt

def stream_handler(message):
  
   entry_len = len(message["path"])
   entry = message["path"]
   
   if(message and message['data'] != None):

        home = db.child("%s"%message["path"]).get().val()

        if isinstance(home, dict):
            print("true")
        else:
            user = entry.split('/')[2]
            
            dest = db.child("uploads").child(user).child("dest").get().val()
            work = db.child("uploads").child(user).child("work").get().val()
            unique = db.child("uploads").child(user).child("unique").get().val()

            print(dest)

            geolocator = Nominatim(user_agent="specify_your_app_name_here")
            location = geolocator.geocode(dest, timeout=None)

            lat1 = location.latitude
            lon1 = location.longitude


            """
            Calculate the great circle distance between two points 
            on the earth (specified in decimal degrees)
            """
            csvfile = open('crime_csv_1.csv')
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            crime_score = 0
            radius = 5.00
            mean = 0
            for row in csv_reader:

                mean = mean+int(row[3])

                lat2 = float(row[1])
                lon2 = float(row[2])

                # convert decimal degrees to radians 
                # lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
                

                # haversine formula 
                dlon = radians(lon2 - lon1)
                dlat = radians(lat2 - lat1)
                a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
                c = 2 * asin(sqrt(a)) 
                r = 6371 # Radius of earth in kilometers. Use 3956 for miles
                result = c * r
                print("result = ", result)
                if (result<=radius):
                    crime_score += int(row[3])

            crime_score_normalised = (abs(crime_score-mean)/mean) * 5

            print(crime_score_normalised)


config = {
    "apiKey": " AIzaSyDStzGJEAUy-Js1vnW2IygbiXl43cTvElI ",
    "authDomain": "superwiemenfirebaseapp.com",
    "databaseURL": "https://superwiemen.firebaseio.com/",
    "storageBucket": "superwiemen.appspot.com",
    #"serviceAccount": "path/to/serviceAccountCredentials.json"
    }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
st = firebase.storage()

my_stream = db.stream(stream_handler, stream_id="new_posts")
