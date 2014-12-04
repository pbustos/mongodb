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
    "calibration-data": [
      {
        "value": "very good",
        "timestamp": "fecha2"
      }
    ],
    "values": [
      {
        "timestamp": "fecha2",
        "val1": [
          {
            "name": "temp1",
            "units": "degrees Celsius",
            "val": ["9.4"]
          }
        ]
      }
    ]
  }
}

sensors = db.sensors
temp_id = sensors.insert(temp)
