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
while True:

    if mydb.is_connected():
        mycursor = mydb.cursor()
        """mycursor.execute("CREATE TABLE {} ({})".format(settings.TABLE_NAME, "price VARCHAR(255), date DATETIME"))"""
        if (count < 1):
            mycursor.execute("CREATE TABLE {} ({})".format(settings.TABLE_NAME, "price VARCHAR(255), date DATETIME"))   
            count += 1
        sql = "INSERT INTO {} (price, date) VALUES (%s, %s)".format(settings.TABLE_NAME)
        p= si.get_top_crypto()
        price = p["Price (Intraday)"][0]
        i = datetime.datetime.now()
        date = ("%s" % i)
    
        val = (price, date)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
    time.sleep(60)
