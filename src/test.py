from models import SVDModel
from data import RecDataSet
import pandas as pd

dset = RecDataSet()
df = dset.get_data()

print(df.head())
