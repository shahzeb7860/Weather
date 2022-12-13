# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import os
from datetime import datetime
import pymongo
import logging


user_api = "126e98a4dfdacf3fb707ab0a15398072"
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
temp_city_feelslike = ((api_data['main']['feels_like']) - 273.15)
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current temperature feels like is: {:.2f} deg C".format(temp_city_feelslike))

#  -------------   MONGODB   ---------

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = client['Weather']
information =mydb.Weatherinformation
record ={
        'City_name' : location,
        'temp_city' : temp_city,
        'temp_city_feelslike' : temp_city_feelslike,
        'date_time' : date_time
        }

information.insert_one(record)

#  -------------   Logging   ---------


LOG_FILENAME = "LOG.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

logging.info({"City_Name" : location})

logging.info({"date_time" : date_time})

logging.info({"Temp_city" : location})

logging.info({"City_Name" : temp_city})

logging.info({"Temp_city_feelslike" : temp_city_feelslike})




