import unittest
class TestEfficiency(unittest.TestCase):
    """
    test cases
    """
    
    def test_keras_regressor(self):
        # inputs
        epochs = 2
        batch_size = 2
        keras_regressor(epochs, batch_size)
        return
    
    def test_DecisionTreeRegressor(self):
        X = dataf[['systemSizeInDCSTC_KW_', 'azimuth_1', 'tilt_1', 'mod_BIPV1', 
        'mod_bifacial1', 'mod_nameplate_capacity1', 'inverterQuantity_1', 
        'inv_microinv1', 'inv_battery_hybrid1', 'inv_builtin_meter1', 'inv_outputcapacity1', 
        'dc_optimizer', 'ILR', 'TotalModuleQty', 'latitude', 'longitude']]

        y = dataf['mod_efficiency1']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.21, random_state=9, shuffle = True)
        self.assertTrue(all(isinstance(x, (int, float)) for x in dataf))
        return
    
    # stepwise selection
    def test_backward_stepwise(self):
        '''
        backward stepwise selection test
        '''
        # add X and y
        names = 'systemSizeInDCSTC_KW_', 'Up_FrontCashIncentive___', 'azimuth_1', 'tilt_1', 'mod_BIPV1', 'mod_bifacial1', 
        'mod_nameplate_capacity1', 'mod_efficiency1', 'inverterQuantity_1', 'inv_microinv1', 'inv_battery_hybrid1', 'inv_builtin_meter1', 
        'inv_outputcapacity1', 'dc_optimizer', 'ILR', 'TotalModuleQty', 'latitude', 'longitude'
        fun_names = np.array(names)
        stepwise_selection(X, y, fun_names)
        return   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestPairwiseCorrelation)
_ = unittest.TextTestRunner().run(suite)