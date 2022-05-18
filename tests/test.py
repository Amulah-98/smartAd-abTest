import sys
import os
import unittest
import numpy as np
import pandas as pd
import pandas.api.types as ptypes

sys.path.insert(0, '../scripts/')
sys.path.append(os.path.abspath(os.path.join('scripts')))

from data_info import dataframeInfo
from data_preProcess import data_preProcess

df = pd.DataFrame({'numbers': [2, 4, 6, 7, 9], 'letters': ['a', 'b', 'c', 'd', 'e'],
                   'floats': [0.2323, -0.23123, np.NaN, np.NaN, 4.3434]})

class TestCases(unittest.TestCase):

   def test_class_creation(self):
        data_preProcessing = dataframeInfo(df)
        self.assertEqual(df.info(), dataframeInfo.df.info())

   def test_remove_duplicates(self):
        data_preProcessing = data_preProcess(df)
        data_preProcessing.drop_duplicates()
        self.assertEqual(data_preProcess.df.shape[0], df.shape[0])
        
   def test_show_data_information(self):
        data_preProcessing = data_preProcessing_script(df)
        data_preProcessing.show_data_information()
        self.assertEqual(
            dataframeInfo.df.info(), df.info())
   
   def test_colums_WithMissingValue(self):
        data_preProcessing = data_preProcess(df)
        data_preProcessing.colums_WithMissingValue()
        
   def test_list_column_names(self):
        data_preProcessing = data_preProcess(df)
        data_preProcessing.list_coloumn_names()
        self.assertEqual(
            data_preProcessing.df.columns.any(), df.columns.any())
        self.assertTrue(data_preProcess.df.isna().sum().sum() != 0)
        
    def test_remove_duplicates(self):
        data_preProcessing = data_preProcess(df)
        data_preProcessing.drop_duplicates()
        self.assertEqual(data_preProcessing.df.shape[0], df.shape[0])
        
if __name__ == '__main__':
    unittest.main()















