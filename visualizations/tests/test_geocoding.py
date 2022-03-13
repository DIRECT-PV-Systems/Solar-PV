import unittest

import pandas as pd
import numpy as np
import csv
import ast

#geocoding packages and functions
import geopy
from geopy.geocoders import Nominatim

from visualizations.geocoding import assign_lat_long_columns, create_save_files, find_unique_cities, geocode_full, geocode_save, geocode_unique, read_data
locator = Nominatim(user_agent= 'starczyn@uw.edu') #change this at the end
#Nominatim limits geocoding extracts to one per second
from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)


class TestReadData(unittest.TestCase):

    #smoke test
    def test_smoke(self):
        file_path = 'data/TTS_sample.csv'
        read_data(file_path)

    # test that input is a file path
    def test_input(self):
        file_path = pd.DataFrame([1, 2, 3])
        with self.assertRaises(TypeError):
            read_data(file_path)

    #check state column exists
    def test_column_state(self):
        file_path = 'tests/no_state.csv'
        with self.assertRaises(KeyError):
            read_data(file_path)

    #check city column exists
    def test_column_state(self):
        file_path = 'tests/no_city.csv'
        with self.assertRaises(KeyError):
            read_data(file_path)

class TestFindUniqueCities(unittest.TestCase):

    # test that input is a pandas dataframe
    def test_input(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            find_unique_cities(data)
    
    #check city_state_country column exists
    def test_column_state(self):
        file_path = 'tests/no_city.csv'
        data  = pd.DataFrame(file_path)
        with self.assertRaises(KeyError):
            find_unique_cities(data)


class TestCreateSaveFiles(unittest.TestCase):

    #smoke test
    def test_smoke(self):
        create_save_files()


class TestGeoCodeSave(unittest.TestCase):

    #smoke test
    def test_smoke(self):
        file_path1 = 'tests/no_city.csv'
        file_path2 = 'tests/no_state.csv'
        files = [file_path1, file_path2]
        data  = pd.DataFrame(file_path1)
        geocode_save(data, files)

    def test_files_length(self):
        file_path1 = 'tests/no_city.csv'
        files = [file_path1]
        data  = pd.DataFrame(file_path1)
        with self.assertRaises(KeyError):
            geocode_save(data)


class TestGeocodeUnique(unittest.TestCase):

    # test that input is a pandas dataframe
    def test_input(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            geocode_unique(data)
    
    # test that length of geocodes matches length of unique cities
    def test_input(self):
        unique_cities = pd.read_csv('data/unique_cities_sample.csv')
        geopy_df = pd.read_csv('data/TTS_sample.csv')
        with self.assertRaises(AttributeError):
            geocode_unique(unique_cities)

class TestAssignLatLongColumns(unittest.TestCase):

    # test coordinates column exists
    def test_column_coordinates(self):
        unique_geo_df = pd.DataFrame({'State' == ['WA']})
        with self.assertRaises(KeyError):
            assign_lat_long_columns(unique_geo_df)

    # test coordinates column is filled
    def test_coordinates_filled(self):
        unique_geo_df = pd.DataFrame({'coordinates':[]})
        with self.assertRaises(AttributeError):
            geocode_unique(unique_geo_df)


class TestGeocodeFull(unittest.TestCase):

    # test that input is a pandas dataframe
    def test_data_type(self):
        data = [1, 2, 3]
        unique_geo_df = pd.DataFrame({'coordinates':[]})
        with self.assertRaises(TypeError):
            geocode_full(data, unique_geo_df)

    def test_unique_geo_df_type(self):
        data = pd.DataFrame({'coordinates':[]})
        unique_geo_df = [1, 2, 3]
        with self.assertRaises(TypeError):
            geocode_full(data, unique_geo_df)

    def test_unique_geo_df_type(self):
        data = pd.DataFrame({'city_state_country':["Washington D.C., DC, USA", "OCEANSIDE, CA, USA"]})
        unique_geo_df = pd.DataFrame({'coordinates':["(38.8950368, -77.0365427)"]})
        with self.assertRaises(AttributeError):
            geocode_full(data, unique_geo_df)

class TestGeocodeGo(unittest.TestCase):

    #smoke test
    def test_smoke(self):
        data_file_path = 'data/TTS_sample.csv'
        read_data(data_file_path)

    # test that input is a file path
    def test_input(self):
        data_file_path = pd.DataFrame([1, 2, 3])
        with self.assertRaises(TypeError):
            read_data(data_file_path)
