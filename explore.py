import csv
import pandas as pd 



TEST_FILE = "./data/train.txt"



# <<-------------------------------------------------------->>
# Step 1. Data Pre-Processing

def feature_selection_imps(file_path):

	matrix = [] 
	header = ['bid_id',
				  'ipinyou_id',
				  'timestamp',
				  'hour',
				  'browser_chrome',
				  'browser_ie',
				  'browser_safari',
				  'browser_firefox',
				  'mobile',
				  'iphone',
				  'ipad',
				  'android',
				  'windows',
				  'linux',
				  'region_id',
				  'ad_exchange',
				  'domain',
				  'ad_slot_id',
				  'ad_slot_size',
				  'ad_slot_visibility',
				  'ad_slot',
				  'ad_slot_floor_price',
				  'paying_price']
	matrix.append(header)	

	with open(file_path) as file:
		csv_reader = csv.reader(file, delimiter = '\t')
		for row in csv_reader:

			#label the attributes
			bid_id = row[0]
			timestamp = row[1]
			log_type = row[2]
			ipinyou_id = row[3]
			useragent = row[4]
			ip_address = row[5]
			region_id = row[6]
			city_id = row[7]
			ad_exchange = row[8]
			domain = row[9]
			url = row[10]
			anonymous_url_id = row[11]
			ad_slot_id = row[12]
			ad_slot_width = row[13]
			ad_slot_height = row[14]
			ad_slot_visibility = row[15]
			ad_slot = row[16]
			ad_slot_floor_price = row[17]
			creative_id = row[18]
			bidding_price = row[19]
			paying_price = row[20]
			key_page_url = row[21]
			advertiser_id = row[22]
			user_tags = row[23]

			# create derivative attributes
			year = timestamp[0:5]
			month = timestamp[5:7]
			day = timestamp[7:9]
			hour = timestamp[8:10]
			minute = timestamp[10:12]


			if 'Chome' in useragent:
				browser_chrome = 1
			else:
				browser_chrome = 0

			if 'MSIE' in useragent:
				browser_ie = 1
			else:
				browser_ie = 0

			if 'Safari' in useragent:
				browser_safari = 1
			else:
				browser_safari = 0

			if 'Firefox' in useragent:
				browser_firefox = 1
			else:
				browser_firefox = 0
			
			if 'Mobile' in useragent:
				mobile = 1
			else:
				mobile = 0

			if 'iPhone' in useragent:
				iphone = 1
			else:
				iphone = 0

			if 'iPad' in useragent:
				ipad = 1
			else:
				ipad = 0

			if 'Android' in useragent:
				android = 1
			else:
				android = 0

			if 'Windows NT' in useragent:
				windows = 1
			else:
				windows = 0

			if 'Linux' in useragent:
				linux = 1
			else:
				linux = 0

			ad_slot_size = str(ad_slot_width)+'x'+str(ad_slot_height)

			vector = [bid_id,
					  ipinyou_id,
					  timestamp,
					  hour,
					  browser_chrome,
					  browser_ie,
					  browser_safari,
					  browser_firefox,
					  mobile,
					  iphone,
					  ipad,
					  android,
					  windows,
					  linux,
					  region_id,
					  ad_exchange,
					  domain,
					  ad_slot_id,
					  ad_slot_size,
					  ad_slot_visibility,
					  ad_slot,
					  ad_slot_floor_price,
					  paying_price]
			matrix.append(vector)

	df = pd.DataFrame(matrix)
	df.columns = matrix[0]
	df = df.ix[1:]
	print(df)


	return 






feature_selection_imps(TEST_FILE)






"""
<<-------------------------------------------------------->>
TO DO: create dataframe, extract and convert all variables
TO DO: save dataframe as binary files
"""