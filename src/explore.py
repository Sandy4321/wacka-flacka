import os
import pickle
import pandas as pd

from preprocessing import feature_selection_imps

TEST_PATH = "./data/mini_test.txt"
TRAIN_PATH = "~/Data/ipinyou/1458/train.log.txt"

# <<-------------------------------------------------------->>
# Step 2. Data Exploration
# <<-------------------------------------------------------->>

print("...Reading dataframe from pickle...")
df2 = pd.read_pickle("./data/df.pickle")
print(df2.head())





"""
<<-------------------------------------------------------->>
TO DO: create dataframe, extract and convert all variables
TO DO: save dataframe as binary files
"""