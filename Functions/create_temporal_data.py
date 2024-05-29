import pandas as pd
import os

def read_csv_to_dataframe(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")

def process_temporal_data(df, datetime_column='DateTime_x'):
    if datetime_column not in df.columns:
        raise ValueError(f"Column {datetime_column} does not exist in the dataframe.")
    
    # Convert to datetime
    df[datetime_column] = pd.to_datetime(df[datetime_column])
    
    # Set datetime column as index
    df.set_index(datetime_column, inplace=True)
    
    # Example: Resample the data to daily frequency, aggregating with mean
    daily_df = df.resample('D').mean()
    
    return daily_df

def store_temporal_data(df, output_path):
    try:
        df.to_csv(output_path)
        print(f"Processed data saved to {output_path}")
    except Exception as e:
        raise Exception(f"An error occurred while saving the file: {e}")

def main():
    input_file = '../Data/Processed/final_merged_data.csv'
    output_file = '../Data/Temporal/final_merged_data_daily.csv'

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        # Read the CSV file
        df = read_csv_to_dataframe(input_file)
        
        # Process the temporal data
        processed_df = process_temporal_data(df, datetime_column='DateTime_x')
        
        # Store the processed data
        store_temporal_data(processed_df, output_file)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()