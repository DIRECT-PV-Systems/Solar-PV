import unittest
import pandas as pd

from visualizations.visualizations import get_cost_total, get_eff_average

class TestImportData(unittest.TestCase):

    #smoke test
    def test_smoke(self):
        file_path = 'visualizations/data/TTS_sample.csv'
        import_data(file_path)

    # test that input is a file path
    def test_input(self):
        file_path = pd.DataFrame([1, 2, 3])
        with self.assertRaises(TypeError):
            import_data(file_path)

class TestGetEffAvg(unittest.TestCase):

    # test that input is a pandas dataframe
    def test_input(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            get_eff_average(data)

class TestGetReportedCosts(unittest.TestCase):

    # test that input is a pandas dataframe
    def test_input(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            get_eff_average(data)

class TestGetCostAverage(unittest.TestCase):

    # test that input is a pandas dataframe
    def test_input(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            get_cost_average(data)

class TestGetCostAverage(unittest.TestCase):

    # test that input is a pandas dataframe
    def test_input(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            get_cost_average(data)

class TestGetCostTotal(unittest.TestCase):

    # test that input is a pandas dataframe
    def test_input(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            get_cost_total(data)