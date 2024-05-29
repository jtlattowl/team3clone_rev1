#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd

# Use the following functions to load in the ERCOT data from 2010 to 2024 into a single dataframe

def list_files_in_directory(directory):
    """
    List all files in the given directory with error handling.

    Parameters:
    directory (str): The path to the directory.

    Returns:
    list: A list of filenames in the directory.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    if not os.access(directory, os.R_OK):
        raise PermissionError(f"The directory {directory} is not readable.")
    return os.listdir(directory)


def filter_xlsx_files(files):
    """
    Filter out the .xlsx files from a list of files.
    
    Parameters:
    files (list): A list of filenames.
    
def read_xlsx_files_to_dataframes(directory, xlsx_files):
    """
    Read .xlsx files into dataframes with error handling.

    Parameters:
    directory (str): The path to the directory containing the files.
    xlsx_files (list): A list of .xlsx filenames.

    Returns:
    list: A list of dataframes.
    """
    dataframes = []
    for file in xlsx_files:
        file_path = os.path.join(directory, file)
        if not os.path.exists(file_path):
            print(f"Warning: The file {file_path} does not exist.")
            continue
        if not os.access(file_path, os.R_OK):
def combine_dataframes(dataframes):
    """
    Combine a list of dataframes into a single dataframe.

    Parameters:
    dataframes (list): A list of dataframes.

    Returns:
    DataFrame: A combined dataframe.
    """
    if not dataframes:
        raise ValueError("No dataframes to combine.")
def main():
    # Define the path to the parent directory
    parent_dir = '..'

    try:
        # List all files in the parent directory
        files_in_parent_dir = list_files_in_directory(parent_dir)

        # Filter out the .xlsx files
        xlsx_files = filter_xlsx_files(files_in_parent_dir)

        # Read .xlsx files into dataframes
        dataframes = read_xlsx_files_to_dataframes(parent_dir, xlsx_files)

        # Combine all dataframes into a single dataframe
        combined_df = combine_dataframes(dataframes)

        # Display the combined dataframe
        print(combined_df.head())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

    # Define the path to the parent directory
    parent_dir = '..'
    
    # List all files in the parent directory
    files_in_parent_dir = list_files_in_directory(parent_dir)
    
    # Filter out the .xlsx files
    xlsx_files = filter_xlsx_files(files_in_parent_dir)
    
    # Read .xlsx files into dataframes
    dataframes = read_xlsx_files_to_dataframes(parent_dir, xlsx_files)
    
    # Combine all dataframes into a single dataframe
    combined_df = combine_dataframes(dataframes)
    
    # Display the combined dataframe
    print(combined_df.head())

    
    
#Use the following functions to read in the fault and status .xls data 

def filter_xls_files(files):
    """
    Filter out the .xls files from a list of files.
    
    Parameters:
    files (list): A list of filenames.
    
    Returns:
    list: A list of .xls filenames.
    """
    return [file for file in files if file.endswith('.xls')]

def read_xls_files_to_dataframes(directory, xls_files):
    """
    Read .xls files into dataframes.
    
    Parameters:
    directory (str): The path to the directory containing the files.
    xls_files (list): A list of .xls filenames.
    
    Returns:
    list: A list of dataframes.
    """
    dataframes = []
    for file in xls_files:
        file_path = os.path.join(directory, file)
        df = pd.read_excel(file_path)
        dataframes.append(df)
    return dataframes

#Use the following functions to read in the scada .csv data 

def filter_csv_files(files):
    """
    Filter out the .csv files from a list of files.
    
    Parameters:
    files (list): A list of filenames.
    
    Returns:
    list: A list of .csv filenames.
    """
    return [file for file in files if file.endswith('.csv')]

def read_csv_files_to_dataframes(directory, csv_files):
    """
    Read .csv files into dataframes.
    
    Parameters:
    directory (str): The path to the directory containing the files.
    csv_files (list): A list of .csv filenames.
    
    Returns:
    list: A list of dataframes.
    """
    dataframes = []
    for file in csv_files:
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)
    return dataframes
def filter_and_save_processed_data():
    """
    Read rpt_2014_combined from the data/processed folder, filter rows with "HB_HOUSTON" in the Settlement Point column,
    and save the filtered dataframe to the data/final folder.
    """
    input_file = '../data/processed/rpt_2014_combined.csv'
    output_file = '../data/final/rpt_2014_combined_filtered.csv'
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file {input_file} does not exist.")
    
    try:
        df = pd.read_csv(input_file)
        filtered_df = df[df['Settlement Point'] == 'HB_HOUSTON']
        filtered_df.to_csv(output_file, index=False)
        print(f"Filtered data saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")



# In[ ]:




