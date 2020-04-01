from surprise import SVD
from surprise.model_selection import GridSearchCV
from surprise.dump import dump, load


class SVDModel:
    def __init__(self):
        self.model = SVD()
        self.name = 'Singular Value Decomposition'

    def train(self, data, n_epochs=[5, 10], lr_all=[
            0.002, 0.005], reg_all=[0.4, 0.5], cv=3):
        param_grid = {'n_epochs': n_epochs,
                      'lr_all': lr_all, 'reg_all': reg_all}
        gs = GridSearchCV(self.model, param_grid,
                          measures=['rmse', 'mae'], cv=cv)
        gs.fit(data)
        gs.best_params['rmse']
        self.model = gs.best_estimator['rmse']

    def predict(self, **kwargs):
        self.model.predict(**kwargs)

    def save(file_name, predictions=None, algo=None, verbose=0):
        dump(file_name, predictions, algo, verbose)

    def load(file_name):
        load(file_name)
