import os
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#from preprocessing import feature_selection_imps

#TEST_PATH = "./data/mini_test.txt"
#TRAIN_PATH = "~/Data/ipinyou/1458/train.log.txt"
CHARTS_DIR_PATH = './charts/'
TABLES_DIR_PATH = './tables/'
DATA_PATH = './data/'

# <<-------------------------------------------------------->>
# Step 2. Data Exploration
# <<-------------------------------------------------------->>

print("...Reading dataframe from pickle...")
df = pd.read_pickle("./data/df.pickle")
print("...Done reading...")
#print(df.head())


def histogram(feature):
		vc = df[feature].value_counts()
		freq = vc.values

		plt.hist(freq)
		plt.savefig(CHARTS_DIR_PATH + ('the-%s-histogram.png' % feature))
		plt.clf()

def piechart(feature):
	vc = df[feature].value_counts()
	vc = vc.sort_index()

	labels = vc.index.values
	fracs = vc.values
	plt.pie(fracs, labels=labels, autopct='%1.1f%%')
	plt.savefig(CHARTS_DIR_PATH + ('the_%s-pie_chart.png' % feature))
	plt.clf()


	# TIMESTAMP
	print("...Counting events per hour...")
	events_per_hour = df['hour'].value_counts()
	events_per_hour = events_per_hour.sort_index()

	events_per_hour.plot()
	plt.savefig(CHARTS_DIR_PATH + 'de_events-per-hour.png')
	plt.clf()

print("============================")
print("...Building the graphs now...")
print("============================")

# FREQUENCY
histogram('ipinyou_id')
print("--First histogram with ID's finished...")

# BROWSER
num_firefox = df['browser_firefox'].sum()
num_safari = df['browser_safari'].sum()
num_ie = df['browser_ie'].sum()
num_chrome = df['browser_chrome'].sum()
#num_other = df['browser_other'].sum()

ind = np.array([0,1,2,3 #,4
	])
width = 0.75
fig, ax = plt.subplots()
rects = ax.bar(left=ind,
			   height=[num_firefox, num_safari, num_ie, num_chrome #, num_other
			   ],
			   width=width)
ax.set_xticks(ind + (width/2))
ax.set_xticklabels(['Firefox', 'Safari', 'IE', 'Chrome' #, 'Other'
					])
plt.savefig(CHARTS_DIR_PATH + 'the_browser-distribution.png')
plt.clf()
print("--Browser distribution finished...")

# MOBILE VS NONMOBILE
num_mobile = df['mobile'].sum()
num_nonmobile = df['mobile'].count() - num_mobile

labels = 'Mobile', 'Non-mobile'
fracs = [num_mobile, num_nonmobile]
plt.pie(fracs, labels=labels)
plt.savefig(CHARTS_DIR_PATH + 'the_mobile-vs-nonmobile.png')
plt.clf()
print("--Mobile vs. Non-Mobile chart finished...")

"""
# REGIONS AND CITIES
num_regions = len(df['region_id'].unique())
num_cities = len(df['city_id'].unique())
print('### REGIONS AND CITIES ###')
print('Number of unique regions: %s' % str(num_regions))
print('Number of unique cities: %s' % str(num_cities))
print()
print('--')
"""
# AD EXCHANGE ID
print("...Counting the ad exchanges and compressing into pie....")
piechart('ad_exchange')
print("--Ad Exchange chart finished...")

# DOMAIN
histogram('domain')

# URL
histogram('url')

# AD SLOT ID
histogram('ad_slot_id')

# AD SLOT SIZE
piechart('ad_slot_size')

# AD SLOT VISIBILITY
piechart('ad_slot_visibility')

# AD SLOT
piechart('ad_slot')

# AD SLOT FLOOR PRICE
histogram('ad_slot_floor_price')

# CREATIVE ID
print(df['creative_id'].value_counts())

# KEY PAGE URL

# ADVERTISER ID

# USER TAGS

