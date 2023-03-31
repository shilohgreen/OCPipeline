import firebase_admin
from firebase_admin import credentials, db

#Firebase stuff
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{

    'databaseURL':'https://occupeye-dedb8-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('/').child('Locations').child('StudyRoom1')

def sendData():
    ref.set({
        "Locations": {
            "Block 55" : {
                "Level-7":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                }
            },
            "Block 57" : {}
        }
    })

