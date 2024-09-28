import pandas as pd
import numpy as np 

# Function to load all Time Series Files and save in a dictionary

def load_raw_data(ids, data_path='./data/csv/'):
    data_dict = {}

    for sample in ids:
        dyn_path = f'{data_path}{sample}/dynamic.csv'
        stat_path = f'{data_path}{sample}/static.csv'
        demo_path = f'{data_path}{sample}/demo.csv'

        # Initialize a container for each sample
        sample_data = {}

        # Check if files exist before reading
        if pd.io.common.file_exists(dyn_path):
            sample_data['dynamic'] = pd.read_csv(dyn_path, header=[0, 1])
        else:
            print(f"Dynamic data not found for sample {sample}")

        if pd.io.common.file_exists(stat_path):
            sample_data['static'] = pd.read_csv(stat_path)
        else:
            print(f"Static data not found for sample {sample}")

        if pd.io.common.file_exists(demo_path):
            sample_data['demographic'] = pd.read_csv(demo_path)
        else:
            print(f"Demographic data not found for sample {sample}")

        # Store the sample's data in the main dictionary
        data_dict[sample] = sample_data

    return data_dict


# Function to Create Clean Static Features Data Frame

def extract_icd_codes(all_data):
    data_frames = []
    for stay_id, data in all_data.items():
        static_data = data['static']
        static_data.columns = static_data.iloc[0]  # Use the first row as column headers
        static_data = static_data.drop(static_data.index[0])  # Drop the first row
        condition_presence = static_data.iloc[0].to_frame().T  # Take the remaining data, convert to DataFrame
        condition_presence.index = [stay_id]  # Set stay_id as the index
        data_frames.append(condition_presence)
    static_features = pd.concat(data_frames)  # Concatenate all DataFrames
    return static_features


# Function to Extract the Dynamic Data to a Dictionary
def extract_dynamic_data_dict(all_data):
    dynamic_data = {}
    for stay_id, data in all_data.items():
        # Extract and store the dynamic data for each stay_id
        dynamic_data[stay_id] = data['dynamic']
    return dynamic_data


# Function to Extract the Dynamic Data to a Data Frame
def extract_demographic_features(all_data):
    demographic_data_frames = []
    for stay_id, data in all_data.items():
        demographic_data = data['demographic']
        demographic_data.index = [stay_id]  # Set stay_id as the index
        demographic_data_frames.append(demographic_data)
    demographic_features = pd.concat(demographic_data_frames)  # Concatenate all DataFrames
    return demographic_features

# Function for creating summary features out of dynamic data
def summarize_dynamic_features(all_data):
    # Initialize an empty dictionary to hold only the dynamic data
    dynamic_data = {stay_id: data['dynamic'] for stay_id, data in all_data.items()}

    # List to hold each row of summary statistics
    data_rows = []

    # Loop through each stay_id in the dynamic_data dictionary
    for stay_id, dataframe in dynamic_data.items():
        # Dictionary to hold the stats for this stay_id
        stats = {'stay_id': stay_id}

        # Helper function to calculate statistics for a given section
        def calc_stats(section, key):
            if key in dataframe.columns.get_level_values(0):
                section_data = dataframe.xs(key, axis=1, level=0, drop_level=False)
                stats[f'{key.lower()}_mean'] = section_data.mean().mean()
                stats[f'{key.lower()}_std'] = section_data.std().mean()
                stats[f'{key.lower()}_min'] = section_data.min().min()
                stats[f'{key.lower()}_max'] = section_data.max().max()

        # Extract statistics for each section
        for section in ['MEDS', 'CHART', 'PROC', 'OUT']:
            calc_stats(dataframe, section)

        # Append the stats dictionary to the list of data rows
        data_rows.append(stats)

    # Create a DataFrame from the list of rows
    sum_dynamic_features = pd.DataFrame(data_rows)

    # Set the stay_id as the index of the DataFrame if desired
    sum_dynamic_features.set_index('stay_id', inplace=True)

    return sum_dynamic_features