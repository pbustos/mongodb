# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 20:15:46 2014

@author: pbustos
"""

import sys
import json
import datetime
from pymongo import MongoClient

client = MongoClient()
db = client.test_database

temp = {
  "Sensor": {
    "type": "temperature",
    "timestamp": "fecha1",
      "localization": [
        {
          "x": "23",
          "y": "54",
          "z": "44",
          "timestamp": "fecha3"
        }
      ],
    "sensor-data": [
      {
        "name": "temperature",
        "calibration": "good",
        "timestamp": "fecha2",
        "units": "grados Celsius"
      },
      {
        "name": "humidity",
        "calibration": "fair",
        "timestamp": "fecha2",
        "units": "porcentaje"
      }
    ],
    "readings": [
      {
        "timestamp": "fecha2",
        "values" : ["34", "43" ]
      }
    ]
  }
}

sensors = db.sensors
#temp_id = sensors.insert(temp)
#list(sensors.find( { "_id": temp_id}))
#
def insertReadings(num):
    for i in range(num):
        v = np.random.rand(2)
        sensors.update( { "_id": temp_id}, {"$push": {"Sensor.readings": \
        {"timestamp":datetime.datetime.utcnow() , "values" : [str(v[0]),str(v[1])] }}})

insertReadings(10000)