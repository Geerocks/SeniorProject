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

p= si.get_top_crypto()
price = p["Price (Intraday)"][0]
print(price)
