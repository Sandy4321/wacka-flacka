#import os 
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#import tensorflow as tf 
import pandas as pd 

#DATA_FILE = '~/Data/ipinyou/1458/train.log.txt'
# train = pd.read_csv(DATA_FILE, sep = "/t")
# df = train.head()
# df.to_csv('./data/train.txt')

# Step 1. Extract data to frame 

data = pd.read_csv('./data/train.txt', engine = 'python')
columns = data.columns
print(data.describe)
print(columns)


"""
<<-------------------------------------------------------->>
TO DO: create dataframe, extract and convert all variables
TO DO: save dataframe as binary files
"""