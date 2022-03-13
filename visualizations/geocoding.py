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

def create_geocode_csvs():
    #create the blank csv, only run once
    #the first csv stores the geocoded data
    f = open("/home/starczyn/Solar-PV/visualizations/data/TTS_data_geocoded_sample.csv", "w")
    writer = csv.DictWriter(f, fieldnames= ['geopy location', 'coordinates'])
    writer.writeheader()
    f.close()
    #second csv stores cities that cannot be geocoded due to error: typos, misspellings, etc.
    #the user could go back and fix these manually if desired after the code runs once
    f = open("/home/starczyn/Solar-PV/visualizations/data/TTS_data_error_cities_sample.csv", "w")
    writer = csv.DictWriter(f, fieldnames= ['location'])
    writer.writeheader()
    f.close()
