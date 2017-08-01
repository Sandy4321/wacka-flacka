import os
import pandas as pd

from preprocessing import feature_selection_imps

TEST_PATH = "./data/mini_test.txt"
TRAIN_PATH = "../../Data/ipinyou/1458/train.log.txt"

# <<-------------------------------------------------------->>
# Step 2. Data Exploration
# <<-------------------------------------------------------->>

feature_selection_imps(TRAIN_PATH)





"""
<<-------------------------------------------------------->>
TO DO: create dataframe, extract and convert all variables
TO DO: save dataframe as binary files
"""