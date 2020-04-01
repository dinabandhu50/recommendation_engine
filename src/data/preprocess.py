import pandas as pd
from sklearn.preprocessing import LabelEncoder


def read_raw_data(fname='data/raw/clickstream_data.csv'):
    dframe = pd.read_csv(fname)
    return dframe


def preprocess_data(dframe):
    dframe = dframe.copy()
    cols_rec = ['productID', 'sessionId', 'eventType']
    # choose only 3 relavent columns
    dframe = dframe[cols_rec]
    # fillna
    df['productID'] = df['productID'].fillna(0).astype('int32')
    # converting string value to numeric value
    df['ratings'] = df['eventType'].apply(
        lambda x: 1 if x == 'pageView' else (2 if x == 'cart' else 3))
    # label encoder
    enc = LabelEncoder()
    df['userID'] = enc.fit_transform(df['sessionId'])
    # final data frame
    df_final = df[['userID', 'productID', 'ratings']]
    return df_final
