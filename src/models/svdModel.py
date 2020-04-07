from surprise import SVD
from surprise.model_selection import GridSearchCV
from surprise.dump import dump, load
import pickle
import sys
import os

sys.path.insert(1, os.getcwd())


class SVDModel:
    def __init__(self):
        self.model = SVD()
        self.name = 'Singular Value Decomposition'

    def best_estimator_gridsearchCV(self, data, n_epochs=[5, 10], lr_all=[
            0.002, 0.005], reg_all=[0.4, 0.5], cv=3):
        param_grid = {'n_epochs': n_epochs,
                      'lr_all': lr_all, 'reg_all': reg_all}
        gs = GridSearchCV(self.model, param_grid,
                          measures=['rmse'], cv=cv)
        gs.fit(data)
        gs.best_params['rmse']
        return params

    def train(self, *args, **kwargs):
        self.model.fit(*args, **kwargs)

    def predict(self, *args, **kwargs):
        self.model.predict(*args, **kwargs)

    def test(self, *args, **kwargs):
        return self.model.test(*args, **kwargs)
    # def save(self, file_name=None, predictions=None, algo=None, verbose=0):
    #     dump(file_name, predictions, algo, verbose)

    # def load(self, file_name):
    #     dump.load(file_name)
