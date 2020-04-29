from yahoo_fin import stock_info as si
import time
import datetime
import mysql.connector
import settings

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gaurav",
    database="stockprice",
    charset = 'utf8'
)
count = 0

p= si.get_live_price("spy")

print(p)
