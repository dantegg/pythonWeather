#coding:utf-8

import sys
sys.path.append("..")
from connectDB import connectDB

testDB = connectDB

testWeatherRecord = {
        "collectTime": '2016-10-16',
        "ctemp":'22'
    }


testconnection = testDB.connectMongo()
testDB.saveWeather(testWeatherRecord,testconnection)
testDB.printWeather(testconnection)