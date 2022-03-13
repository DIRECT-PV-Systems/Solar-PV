import pandas as pd
import numpy as np
import csv
import ast

#geocoding packages and functions
import geopy
from geopy.geocoders import Nominatim
locator = Nominatim(user_agent= 'starczyn@uw.edu') #change this at the end
#Nominatim limits geocoding extracts to one per second
from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

def read_data(file_path):

    """
    Creates pandas dataframe from .csv in path specified
    Assumes city, state are columns in file
    Adds 'city_state_country' column to improve geocoding
    :param .csv file_path: file path of .csv data
    """
    #reading in the dataset
    data = pd.read_csv(file_path)
    #adding a column to make the location more compatible with geopy and reduce mislocating
    data['city_state_country'] = data['hostCustomerCity'] + ', ' + data['state'] + ', USA'
    return data

def find_unique_cities(data):
    """
    Creates pandas dataframe of unique locations
    Sends unique cities to a .csv for reference
    :param dataframe-pandas data: dataframe containing locations
    """
    #create a dataframe of unique locations
    unique_data = data['city_state_country'].unique()
    unique_cities = pd.DataFrame(data = unique_data, columns = ['city_state_country'])
    #send the results to a csv for reference
    unqiue_cities_csv = pd.DataFrame.to_csv(unique_cities, 
    '/home/starczyn/Solar-PV/visualizations/data/unique_cities_sample.csv')
    return unique_cities

def create_save_files():
    """
    Creates csv files to save geocoding and location that produce error with Nominatim
    This should only be run if a blank csvs are needed
    """
    #geopy csv
    f = open("/home/starczyn/Solar-PV/visualizations/data/TTS_geocoded_sample.csv", "w")
    writer = csv.DictWriter(f, fieldnames= ['geopy location', 'coordinates'])
    writer.writeheader()
    f.close()

    #csv of locations that produce erros
    f = open("/home/starczyn/Solar-PV/visualizations/data/TTS_error_cities_sample.csv", "w")
    writer = csv.DictWriter(f, fieldnames= ['location'])
    writer.writeheader()
    f.close()

#store csvs for geocoding
geocode_unique_csv = '/home/starczyn/Solar-PV/visualizations/data/TTS_geocoded_sample.csv'
error_cities_csv = "/home/starczyn/Solar-PV/visualizations/data/TTS_error_cities_sample.csv"

files = [geocode_unique_csv, error_cities_csv]

def geocode_save(row, file = files):

    """
    Saves each geocoded location to the csv file
    Sends unique cities to a .csv for reference
    :param series-pandas row: row of pandas dataframe
    :param array-files file: array of files
    """

    current_csv = pd.read_csv(file[0], index_col = 0)
    
    index = row.name
    loc = row['city_state_country']
    
    #length of csv is number of rows that are done
    csv_length = len(current_csv) 
    
    try: 
        #if the row has already been geocoded the row is returned back     
        if index <= csv_length - 1:
            
            with open(file[0], 'a') as geopy_csv:
                append = csv.writer(geopy_csv)
                geopy_csv.close()
                
            return current_csv.iloc[index].values[0]

        #if the row has not been geocoded, the row is geocoded and saved to the csv
        else:
            
            location = geocode(loc)

            with open(file[0], 'a') as geopy_csv:
                append = csv.writer(geopy_csv)
                append.writerow(location)
                geopy_csv.close()

            return "({},{})".format(location.longitude,location.latitude)
    
    except:

            with open(file[0], 'a') as geopy_csv:
                append = csv.writer(geopy_csv)
                append.writerow(['nan'])
                geopy_csv.close()
            
            with open(file[1], 'a') as error_csv:
                append = csv.writer(error_csv)
                append.writerow([loc])
                error_csv.close()

            return "({},{})".format('nan','nan')

def geocode_unique(unique_cities):
    
    """
    Iterates through each unique city to assign geocoding
    Sends complete geopy locations to a .csv file for reference
    Concatonates geopy locations with unique location dataframe
    Sends concatonation to a .csv for reference
    Returns a dataframe of unique locations geocoded
    :param dataframe-pandas unique_cities: dataframe containing unique locations
    """

    for idx, row in unique_cities.iterrows():
        geocode_save(row)

    geopy_df = pd.read_csv('/home/starczyn/Solar-PV/visualizations/data/TTS_geocoded_sample.csv')

    frames = [unique_cities, geopy_df]
    unique_geo_df = pd.concat(frames, axis=1, join="inner")
    unqiue_cities_geocoded = pd.DataFrame.to_csv(unique_geo_df, 
    '/home/starczyn/Solar-PV/visualizations/data/unique_cities_geocoded_sample.csv' )

    return unique_geo_df

def assign_lat_long_columns(unique_geo_df):
    """
    Creates seperate columns for latitude and longitude from geopy location
    :param dataframe-pandas unique_geo_df: dataframe containing unique locations
    """

    for idx, row in unique_geo_df.iterrows():
        try: 
            point = ast.literal_eval(unique_geo_df['coordinates'].iloc[idx])
            latitude, longitude = point
            unique_geo_df.loc[idx,'latitude'] = latitude
            unique_geo_df.loc[idx,'longitude'] = longitude
        except:
            unique_geo_df.loc[idx,'latitude'] = np.nan
            unique_geo_df.loc[idx,'longitude'] = np.nan

    return unique_geo_df

def geocode_full(data, unique_geo_df):

    """
    Uses the geocodes of unique cities to geocode the full dataframe
    :param dataframe-pandas data: dataframe to be geocoded
    :param dataframe-pandas unique_geo_df: dataframe of unique cities geocoded

    """

    for idx1, row in data.iterrows():
        try:
            city = row['city_state_country']
            idx2 = unique_geo_df['city_state_country'].str.contains(city, na = False)
            latitude = unique_geo_df.loc[idx2,'latitude'].values[0]
            longitude = unique_geo_df.loc[idx2,'longitude'].values[0]
            data.loc[idx1, 'latitude'] = latitude
            data.loc[idx1, 'longitude'] = longitude

        except: 
            data.loc[idx1, 'latitude'] = np.nan
            data.loc[idx1, 'longitude'] = np.nan
            
    return data

def geocode_go(data_file_path):
    
    """
    Geocodes in one go based on the file path of the data to be geocoded 
    :param filepath-csv data_file_path): location .csv to be geocoded

    """

    data = read_data(data_file_path)
    unique_cities = find_unique_cities(data)
    geocode_unique_csv = '/home/starczyn/Solar-PV/visualizations/data/TTS_geocoded_sample.csv'
    error_cities_csv = "/home/starczyn/Solar-PV/visualizations/data/TTS_error_cities_sample.csv"
    files = [geocode_unique_csv, error_cities_csv]
    unique_geo_df = geocode_unique(unique_cities)
    unique_geo_df = assign_lat_long_columns(unique_geo_df)
    data = geocode_full(data, unique_geo_df)
    
    return data



