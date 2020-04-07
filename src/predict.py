import pickle
from collections import defaultdict
from data import RecDataSet
from surprise import Reader, Dataset
from surprise.model_selection import train_test_split


def get_top_n(predictions, n=3):
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    return top_n


PATH_MODEL = './src/models/mymodel.pkl'
with open(PATH_MODEL, 'rb') as fid:
    mymodel = pickle.load(fid)

# dataset reading
data_cls = RecDataSet()
df = data_cls.get_data()
# printing
# print(df.head())
# Converting to reader format
reader = Reader()
data = Dataset.load_from_df(df, reader)

# train test split
# Splitting is not needed for recommendation Engine
trainset, testset = train_test_split(data, test_size=0.20, random_state=1)

# Predict from model
# userid, prodid, actual_rating = trainset[5]
# predictions = mymodel.predict(userid, prodid, actual_rating)
# print(testset[5])
# print(predictions)

# Print recommendation
predictions = mymodel.test(testset)
# print(predictions)

top_n = get_top_n(predictions, n=3)

# print the recommendations
for uid, user_ratings in top_n.items():
    print(uid, [iid for (iid, _) in user_ratings])
    # break
