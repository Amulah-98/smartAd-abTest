import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class dataframeMunging:
    ###############################################################################
    # dataframe munging and manipulation script
    ################################################################################
    def __init__(self, df: pd.DataFrame):
        """
            Returns a data munging Object with the passed DataFrame Data set as its own DataFrame
        """
        self.df = df

    def find_sort_using_column(self, column: str) -> pd.DataFrame:
        """
            Returns the objects DataFrame sorted with the specified column
        """
        try:
            return self.df.sort_values(column)
        except:
            print("Failed to sort using the specified column")

    def find_normalized_scale_column(self, column: str) -> pd.DataFrame:
        """
            Returns the objects DataFrames column scaled using MinMaxScaler
        """
        try:
            scale_column_df = pd.DataFrame(self.df[column])
            scale_column_values = scale_column_df.values
            print(
                f'The max and min values of the scaled {column} column are:\n\tmax: {scale_column_df.iloc[:, 0].min()}\n\tmin: {scale_column_df.iloc[:, 0].max()}')
            min_max_scaler = MinMaxScaler()
            scaled_values = min_max_scaler.fit_transform(scale_column_values)
            self.df[column] = scaled_values

            return self.df

        except:
            print("Failed to scale the column")

    def find_standardize_column(self, column: str) -> pd.DataFrame:
        """
            Returns the objects DataFrames column normalized using Normalizer
        """
        try:
            std_column_df = pd.DataFrame(self.df[column])
            std_column_values = std_column_df.values
            standardizer = StandardScaler()
            normalized_data = standardizer.fit_transform(std_column_values)
            self.df[column] = normalized_data

            return self.df
        except:
            print("Failed to standardize the column")
