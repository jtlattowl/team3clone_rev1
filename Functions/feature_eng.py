import pandas as pd
import numpy as np
import os
# import matplotlib.pyplot as plt
# import missingno as msno
# import seaborn as sns

# Define the relative file paths
data_path = '../data/raw/final_merged_data.csv'
df = pd.read_csv(data_path)

# Convert DateTime_x column format
df['DateTime_x'] = pd.to_datetime(df['DateTime_x'])
#keep only 2014
df = df[df['DateTime_x'].dt.year == 2014]


# Set 'DateTime' as the index if it isn't already
df.set_index('DateTime_x', inplace=True)
# Resample the data weekly and calculate the mean of 'WEC: max. Power'
weekly_max_power = df['WEC: max. Power'].resample('W').mean()
# Forward-fill the resampled values to match the original DataFrame's index
df['Weekly Max Power'] = weekly_max_power.reindex(df.index, method='ffill')
# Reset the index if you want to keep 'DateTime' as a column
df.reset_index(inplace=True)