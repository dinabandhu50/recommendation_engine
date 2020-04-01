from preprocess import read_raw_data, preprocess_data


class RecDataSet:
    def __init__(self, ifile='data/raw/clickstream_data.csv', ofile='data/processed/clickstream_processed_data.csv'):
        self.raw_data_path = ifile
        self.processed_data_path = ofile

    def get_data(self):
        dframe = read_raw_data(self.raw_data_path)
        df_final = preprocess_data(dframe)
        return df_final
