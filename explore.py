#import os 
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#import tensorflow as tf 
import pandas as pd 

DATA_FILE = '~/Data/ipinyou/1458/train.log.txt'
train = pd.read_csv(DATA_FILE, sep = "/t")
print("The various axes of the dataframe are: ", train.axes)

"""
<<-------------------------------------------------------->>
TO DO: create dataframe and convert to variables
TO DO: save dataframe and convert to binary files ,perhaps test with heads

"""