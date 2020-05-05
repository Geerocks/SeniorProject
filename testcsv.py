import csv
import datetime
import pprint
import mysql.connector 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gaurav",
    database="netsentiment",
    charset = 'utf8'
)
count = 0
with open('t5.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',')

	start_hour = 15
	start_minute = 2
	start_time = datetime.datetime(2020, 5, 1, start_hour, start_minute)

	time_threshold = start_time
	net_polarity = 0
	segment_polarity_data = {}

	for row in reader:
		# check if tweet time is outside of the last 10 minute time segment
		# if tweet time is outside of the 10-min threshold, move the segment forward by 10 minutes
		# before moving the segment, save the segment-net_polarity data pair
		tweet_time = datetime.datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S')
		if tweet_time >= time_threshold + datetime.timedelta(minutes=1):
			# save segment-net_polarity data pair
			time_threshold_str = datetime.datetime.strftime(time_threshold, '%Y-%m-%d %H:%M:%S')
			segment_polarity_data[time_threshold_str] = net_polarity

			# move segment forward by 10 minutes
			time_threshold += datetime.timedelta(minutes=1)
			net_polarity = 0

		# update polarity (option 1, no error handling)
		net_polarity += int(row['polarity'])

		# # update polarity (option 2, with error handling)
		# # if the polarity doesn't exist, don't update anything (treat it as 0)
		# if row['polarity'] != None and row['polarity'].isdigit():
		# 	try:
		# 		net_polarity += int(row['polarity'])
		# 	except ValueError:
		# 		print("Error. Polarity string is: " + row['polarity'])

		# printing utilities
		# pp = pprint.PrettyPrinter(indent=4)
		# pp.pprint(row)
		# print('\n')
		# print('Datetime: ' + row['created_at'])
		# print('Tweet:\n"' + row['text'] + '"')
		# print('Polarity: ' + row['polarity'])
		# print('\n')
		
	# save the last data pair

	
	time_threshold_str = datetime.datetime.strftime(time_threshold, '%Y-%m-%d %H:%M:%S')
	segment_polarity_data[time_threshold_str] = net_polarity
	for x in segment_polarity_data:
		if mydb.is_connected():
			mycursor = mydb.cursor()
			"""mycursor.execute("CREATE TABLE {} ({})".format(settings.TABLE_NAME, "price VARCHAR(255), date DATETIME"))"""
			if (count < 1):
				mycursor.execute("CREATE TABLE {} ({})".format("t1", "date DATETIME, polarity INT(255)"))   
				count += 1
			sql = "INSERT INTO {} (date, polarity) VALUES (%s,%s)".format("t1")
			date = x
			polarity = segment_polarity_data[x]
			val = (date, polarity)
			mycursor.execute(sql, val)
			mydb.commit()
			mycursor.close()
		