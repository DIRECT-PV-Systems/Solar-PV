import pandas as pd
import numpy as np
import sklearn

from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
# Note - you will need version 0.24.1 of scikit-learn to load this library (SequentialFeatureSelector)
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

import unittest

class TestCost(unittest.TestCase):
    """
    test cases
    """
    # stepwise selection
    def test_one_shot_test_forward_stepwise(self):
        """
        Forward stepwise selection
        """
        df = pd.read_csv('TTS_sample.csv')
        X = df[['systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1',
        'mod_nameplate_capacity1', 'inverterQuantity_1', 'inv_outputcapacity1',
        'ILR', 'TotalModuleQty', 'latitude', 'longitude','mod_efficiency1']]
        y = df['totalInstalledCost___']

        names = 'systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1', 'mod_BIPV1', 'mod_bifacial1', 'mod_nameplate_capacity1', 'mod_efficiency1', 'inverterQuantity_1', 'inv_microinv1', 'inv_battery_hybrid1', 'inv_builtin_meter1', 'inv_outputcapacity1', 'dc_optimizer', 'ILR', 'TotalModuleQty', 'latitude', 'longitude'
        f_names = np.array(names)
        forward_stepwise_selection(X, y, f_names)
        return

    def test_forward_stepwise_input(self):
        df = pd.read_csv('TTS_sample.csv')
        df = df[['systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1',
        'mod_nameplate_capacity1', 'inverterQuantity_1', 'inv_outputcapacity1',
        'ILR', 'TotalModuleQty', 'latitude', 'longitude','mod_efficiency1', 'totalInstalledCost___']]

        # check if string is present
        self.assertTrue(isinstance(x, (int, float)) for x in df)
        return

    def test_one_shot_test_backward_stepwise(self):
        """
        Backward stepwise selection
        """
        df = pd.read_csv('TTS_sample.csv')
        X = df[['systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1', 
        'mod_nameplate_capacity1', 'inverterQuantity_1', 'inv_outputcapacity1', 
        'ILR', 'TotalModuleQty', 'latitude', 'longitude','mod_efficiency1']]
        y = df['totalInstalledCost___']

        names = 'systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1', 'mod_BIPV1', 'mod_bifacial1', 'mod_nameplate_capacity1', 'mod_efficiency1', 'inverterQuantity_1', 'inv_microinv1', 'inv_battery_hybrid1', 'inv_builtin_meter1', 'inv_outputcapacity1', 'dc_optimizer', 'ILR', 'TotalModuleQty', 'latitude', 'longitude'
        f_names = np.array(names)
        backward_stepwise_selection(X, y, f_names)
        return

    def test_backward_stepwise_input(self):
        """
        Checks if strings are present in dataset
        """
        df = pd.read_csv('TTS_sample.csv')
        df = df[['systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1',
        'mod_nameplate_capacity1', 'inverterQuantity_1', 'inv_outputcapacity1',
        'ILR', 'TotalModuleQty', 'latitude', 'longitude','mod_efficiency1', 'totalInstalledCost___']]

        self.assertTrue(isinstance(x, (int, float)) for x in df)
        return

    # random forest regressor
    def test_one_shot_rf(self):
	"""
	One shot test for random forest regressor
	"""
        df = pd.read_csv('TTS_sample.csv')
        X = df[['systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1',
        'mod_nameplate_capacity1', 'inverterQuantity_1', 'inv_outputcapacity1',
        'ILR', 'TotalModuleQty', 'latitude', 'longitude','mod_efficiency1']]
        y = df['totalInstalledCost___']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.21, random_state=9, shuffle = True)

        self.assertTrue(random_forest_reg(X_train, y_train, X_test, y_test))
        return
