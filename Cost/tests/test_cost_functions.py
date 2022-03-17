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

from cost_functions import forward_stepwise_selection
from cost_functions import backward_stepwise_selection
from cost_functions import different_values
from cost_functions import unique_values
from cost_functions import random_forest_reg

class TestCost(unittest.TestCase):
    """
    test cases
    """

    def test_eff_missing_data(self):
        """
        Checks for missing data in efficiency column (indicted with -1)
        """
        missing_val = -1
        df = pd.read_csv('TTS_sample.csv')
        if missing_val in df['mod_efficiency1']:
            self.assertRaises(ValueError)
        return

    # stepwise selection

    # forward stepwise selection
    def test_one_shot_test_forward_stepwise(self):
        """
        Forward stepwise selection: one shot test
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
        """
        Forward stepwise selection: Checks input type; only accepts int/float values
        """
        df = pd.read_csv('TTS_sample.csv')
        df = df[['systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1',
        'mod_nameplate_capacity1', 'inverterQuantity_1', 'inv_outputcapacity1',
        'ILR', 'TotalModuleQty', 'latitude', 'longitude','mod_efficiency1', 'totalInstalledCost___']]

        # check if string is present
        self.assertTrue(isinstance(x, (int, float)) for x in df)
        return

    # backward stepwise selection
    def test_one_shot_test_backward_stepwise(self):
        """
        Backward stepwise selection: one shot test
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
        Backward stepwise selection: Checks input type; only accepts int/float values
        """
        df = pd.read_csv('TTS_sample.csv')
        df = df[['systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1',
        'mod_nameplate_capacity1', 'inverterQuantity_1', 'inv_outputcapacity1',
        'ILR', 'TotalModuleQty', 'latitude', 'longitude','mod_efficiency1', 'totalInstalledCost___']]

        self.assertTrue(isinstance(x, (int, float)) for x in df)
        return

    # different values
    def test_one_shot_test_different(self):
        """
        Different values: one shot test
        """
        alist = [1,3,5]
        blist = [1,3,6]
        self.assertTrue(different_values(alist, blist))

        return

    def test_pattern_test_different(self):
        """
        Different values: pattern test
        """
        alist = [1,3,5]
        blist = [1,3,6]
        diff_list = [5,6]

        if np.allclose(different_values(alist, blist), diff_list):
            print('Passed Pattern Test for Different Values')

        return

    # unique values
    def test_one_shot_test_unique(self):
        """
        Unique values: one shot test
        """
        alist = [1,3,5]
        blist = [1,3,6]
        self.assertTrue(unique_values(alist, blist))

        return

    def test_pattern_test_unique(self):
        """
        Unique values: pattern test
        """
        alist = [1,3,5]
        blist = [1,3,6]
        diff_list = [1,3,5,6]

        if np.allclose(unique_values(alist, blist), diff_list):
            print('Passed Pattern Test for Unique Values')

        return

    # random forest regressor
    def test_one_shot_rf(self):
        """
        Random Forest Regressor: One shot test
        """
        df = pd.read_csv('TTS_sample.csv')
        X = df[['systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1',
        'mod_nameplate_capacity1', 'inverterQuantity_1', 'inv_outputcapacity1',
        'ILR', 'TotalModuleQty', 'latitude', 'longitude','mod_efficiency1']]
        y = df['totalInstalledCost___']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.21, random_state=9, shuffle = True)

        self.assertTrue(random_forest_reg(X_train, y_train, X_test, y_test))
        return
