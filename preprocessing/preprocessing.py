import h5py
import numpy as np    
import matplotlib.pyplot as plt
import pandas as pd
import os

def preprocess_dataset(df, selected_columns=None):
    # strip of "b'" of all strings
    # cols_to_strip = [
    #         'author_id', 'created_at', 'edit_history_tweet_ids', 'entities_annotations', 
    #         'entities_hashtags', 'entities_mentions', 'entities_urls', 'geo_coord_data',
    #         'geo_coord_type', 'geo_placeid', 'img_name', 'img_size', 'in_reply_to_user_id',
    #         'lang', 'media_keys', 'referenced_tweets', 'source', 'text', 'tweet_id', 
    #         'withheld_copyright', 'withheld_countrycode', 'entities_cashtags'
    #         ]    -> was for complete dataset?

    cols_to_strip = ['created_at', 'img_name', 'language', 'referenced_tweets', 'text', 'tweet_id']   

    df[cols_to_strip] = df[cols_to_strip].astype('string')
    df[cols_to_strip] = df[cols_to_strip].replace(to_replace=r'^b\':?(.*)\'$', value=r'\1', regex=True)

    print(df.shape)
    df.dtypes

    # replace string NA to "real" missing value for further analysis
    df = df.replace(r'^NA$', np.nan, regex=True)
    df.isna().sum()

    ## only keep selected_columns here
    if selected_columns is not None:
        df = df.loc[:, selected_columns]

    return df

def load_dataset(subset_name):
    ######## Very basic access to the dataset - let's see what we are working with! #######
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    dataset_path =  os.path.join(parent_dir, f'dataset/{subset_name}.h5')
    raw_dataset = h5py.File(dataset_path,'r+') 

    # Access the 'upper' data - we only have tweet data 
    for item in raw_dataset.keys():
        print("Items: " + item)    
        
    # Access the actual subgroups with data for us - different info we can look at - mostly things provided in Excel by Katharina
    for item in raw_dataset.require_group('tweet_data').keys():
        continue  ### comment this out if you want to see categories we have and use print

    # Access the dataset within the group
    dataset = raw_dataset['tweet_data']  ## excludes unnecessary information - only tweet_data
    
    # Create a dictionary to store column data
    data_dict = {}
        
    # Iterate through the keys (assuming each key is a column name)
    for key in dataset.keys():
        # Access the data for each column
        column_data = dataset[key][:]
            
        # Store the data in the dictionary with the column name as the key
        data_dict[key] = column_data
    
    # Convert the dictionary to a Pandas DataFrame
    df = pd.DataFrame(data_dict)
    return df

