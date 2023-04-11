import firebase_admin
from firebase_admin import credentials, db

#Firebase stuff
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{

    'databaseURL':'https://occupeye-dedb8-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('/')

def sendData():
    ref.set({
        "Locations": {
        'Hostel': {
            "Block 55" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            },
            "Block 57" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            },
            "Block 59" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            }
        }, "College": {
            "Block 55" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            },
            "Block 57" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            },
            "Block 59" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            }
        }, "Library": {
            "Block 55" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            },
            "Block 57" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            },
            "Block 59" : {
                "Level-4-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
                "Level-6-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },"Level-7-Study-Room":{
                    "Room Capacity": "10",
                    "Users": None,        
                    "Colour Grading": "White"
                },
            }
        }
        }
        
    })

sendData()
