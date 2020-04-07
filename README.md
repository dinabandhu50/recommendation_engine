# This repository contains recommendation engine implementation

## Dataset used

We have used movieLens dataset for our project. The dataset can be found in this [link](https://grouplens.org/datasets/movielens/). In this project we have used ml-1m (one million) dataset, the larger version of dataset are also available you can use any version of dataset.

## How to setup conda environment

To make conda yml environment:

```sh
conda env export > conda.yml
```

To create conda environment from yml file:

```sh
conda env create -f conda.yml
```

## How to use

Run all the file from root folder

```sh
python src/train.py
```

or

```sh
python src/predict.py
```

## folder structure

recommendation_engine
