import os
import sys
import pandas as pd
from . import preprocess_data, read_raw_data


sys.path.insert(0, os.getcwd())


class RecDataSet:
    def __init__(self, ifile='./data/raw/clickstream_data.csv', ofile='./data/processed/clickstream_processed_data.csv'):
        self.raw_data_path = ifile
        self.processed_data_path = ofile

    def process(self, directory):
        dframe = read_raw_data(directory)
        df_final = preprocess_data(dframe)
        print(type(df_final))
        return df_final

    def get_data(self):
        return self.process(self.raw_data_path)
