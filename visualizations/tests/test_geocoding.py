import unittest

import pandas as pd
import numpy as np
import csv
import ast

#geocoding packages and functions
import geopy
from geopy.geocoders import Nominatim

from visualizations.geocoding import find_unique_cities
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

    def test_inputs(self):
        # test that inputs are of the correct size
        x_test_row = pd.DataFrame(data=(2, 3, 4, 2))
        X_train = pd.DataFrame([[-1, 0, 4], [1, 0, -1], [9, 0, 1]])
        y_train = pd.DataFrame([[-1, 0, 8]])

        with self.assertRaises(ValueError):
            get_sorted_list(x_test_row, X_train, y_train, 5)


class TestGeoCodeSave(unittest.TestCase):

    def test_x_test_input(self):
        # test that the dataframe has the indexes of y_train
        knn_list = pd.DataFrame(data=(2, 3, 4))
        y_train = pd.DataFrame([[-1, 0, 3]])

        with self.assertRaises(ValueError):
            predict(knn_list, y_train)


class TestGeocodeUnique(unittest.TestCase):

    def test_num_modes(self):
        # test that knn_list returns an error if only one mode exists
        knn_list = pd.DataFrame(data={'distance': [20, 21, 19, 18],
                                      'y_train': [20, 20, 19, 18]})

        with self.assertRaises(ValueError):
            tie_breaker(knn_list)


class TestGeocodeFull(unittest.TestCase):

    def test_k_types(self):
        # test that k list contains only integers
        k_list = [2, 3, 4, 5, 'R', 7]
        df_train = pd.DataFrame(data={'random': [20, 21, 19, 18]})
        df_test = pd.DataFrame(data={'random': [20, 20, 19, 18]})

        with self.assertRaises(TypeError):
            k_selection(df_train, df_test, k_list)

class TestGeocodeGo(unittest.TestCase):

    def test_k_types(self):
        # test that k list contains only integers
        k_list = [2, 3, 4, 5, 'R', 7]
        df_train = pd.DataFrame(data={'random': [20, 21, 19, 18]})
        df_test = pd.DataFrame(data={'random': [20, 20, 19, 18]})

        with self.assertRaises(TypeError):
            k_selection(df_train, df_test, k_list)
