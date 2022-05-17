
import pandas as pd
import numpy as np


class dataframeInfo:
    def __init__(self, df: pd.DataFrame):
        """
            Returns a dataframe Info Object with the passed DataFrame Data
            Parameters
        """
        self.df = df

    def find_matrix_correlation(self):
        '''
            Returns the correlation matrix of the passed Dataframe
        '''
        return self.df.corr()

    def find_memory_usage(self):
        '''
            Returns the memory usage of the passed DAtaframe
        '''
        print(f"Current DataFrame Memory Usage of columns is :")
        return self.df.memory_usage()
