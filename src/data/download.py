import os
import pandas as pd
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(os.path.join(
    os.getcwd(), "coe-solutions-215839-c9b1b2b721c8.json"))

# The below code for setting GOOGLE_APPLICATION_CREDENTIALS only works for jupyter notebook
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../../coe-solutions-215839-c9b1b2b721c8.json"
# os.path.join('/'.join(os.getcwd().split('/')[:-2]), 'coe-solutions-215839-c9b1b2b721c8.json')
# print("[INFO] setting ... \n GOOGLE_APPLICATION_CREDENTIALS =",
#   os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
print("[INFO] current working directory is: ", os.getcwd())
query = '''
SELECT 
* 
FROM 
`coe-solutions-215839.clickstream_dataset.clickstream_data1_cleaned_scheduled` 
LIMIT 
1000
'''

filename = './data/raw/clickstream_data.csv'


def bigquery_to_df(sql=query, filename=filename):
    df = pd.read_gbq(sql, dialect='standard')
    df.to_csv(filename)


if __name__ == '__main__':
    bigquery_to_df()
