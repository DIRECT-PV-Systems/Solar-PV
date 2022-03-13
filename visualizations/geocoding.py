import pandas as pd
import numpy as np
import csv
import ast

#geocoding packages and functions
import geopy
from geopy.geocoders import Nominatim
locator = Nominatim(user_agent= 'starczyn@uw.edu') #change this at the end
#nominatim limits geocoding extracts to one per second
from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

def read_data(file_path):
    
    #reading in the dataset
    data = pd.read_csv(file_path)
    #adding a column to make the location more compatible with geopy and reduce mislocating
    data['city_state_country'] = data['hostCustomerCity'] + ', ' + data['state'] + ', USA'
    return data

def find_unique_cities(data):
    #create a dataframe of unique locations
    unique_data = data['city_state_country'].unique()
    unique_cities = pd.DataFrame(data = unique_data, columns = ['city_state_country'])
    #send the results to a csv for reference
    unqiue_cities_csv = pd.DataFrame.to_csv(unique_cities, '/home/starczyn/Solar-PV/visualizations/data/unique_cities_sample.csv')
    return unique_cities

def create_save_files():
    #create the blank csv, only run once

    f = open("/home/starczyn/Solar-PV/visualizations/data/TTS_geocoded_sample.csv", "w")
    writer = csv.DictWriter(f, fieldnames= ['geopy location', 'coordinates'])
    writer.writeheader()
    f.close()

    f = open("/home/starczyn/Solar-PV/visualizations/data/TTS_error_cities_sample.csv", "w")
    writer = csv.DictWriter(f, fieldnames= ['location'])
    writer.writeheader()
    f.close()

def geocode_save(row, file = files): #row is pandas series: index in dataframe and value of column at the row

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

    for idx, row in unique_cities.iterrows():
        geocode_save(row)

    geopy_df = pd.read_csv('/home/starczyn/Solar-PV/visualizations/data/TTS_geocoded_sample.csv')

    frames = [unique_cities, geopy_df]
    unique_geo_df = pd.concat(frames, axis=1, join="inner")
    unqiue_cities_geocoded = pd.DataFrame.to_csv(unique_geo_df, 
    '/home/starczyn/Solar-PV/visualizations/data/unique_cities_geocoded_sample.csv' )

    return unique_geo_df
            
          

        
