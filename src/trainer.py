import os
import sys
sys.path.insert(1, os.getcwd())
# sys.path.append('./')
sys.path.append('../')


import pickle
import pandas as pd
from data import RecDataSet
# from models import SVDModel
# from surprise import Reader, Dataset
# from surprise.model_selection import train_test_split
from scipy.sparse import csr_matrix

# dataset reading
data_cls = RecDataSet()
df = data_cls.get_data()
# printing
print(df.head())
# # Converting to reader format
# reader = Reader()
# data = Dataset.load_from_df(df, reader)

# # train test split
# # Splitting is not needed for recommendation Engine
# trainset, testset = train_test_split(data, test_size=0.20, random_state=1)

# # Model building
# algo = SVDModel()

# # model selection
# # params = algo.best_estimator_gridsearchCV(trainset)
# # print(params)
# # Training the model
# algo.train(trainset)

# # Saving the model
# PATH_MODEL = './src/models/mymodel.pkl'
# with open(PATH_MODEL, 'wb') as fid:
#     pickle.dump(algo, fid)
