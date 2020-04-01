import pickle

from dataset import RecDataSet
from surprise import Reader, Dataset
from surprise.model_selection import train_test_split, cross_validate, GridSearchCV

# dataset reading
df = RecDataSet()
reader = Reader()
data = Dataset.load_from_df(df, reader)

# train test split
trainset, testset = train_test_split(data, test_size=0.20, random_state=1)

# model selection
