'''
    Here we take all of the fastai models in ./models and record associated statistics and meta-data
'''

import os
import sys
import json
import pickle
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from fastai.vision import *
from fastai.metrics import *
from fastai.basic_data import *


parser = argparse.ArgumentParser(description='Model stats')
parser.add_argument('-m', '--models-path', default='./models', help='Path to models folder')
parser.add_argument('-o', '--output-path', default='./modelstats', help='Path to output folder')
parser.add_argument('-f', '--file-name', default='modelstats.csv', help='File name')
parser.add_argument('-p', '--plot-name', default='modelstats.png', help='File name')
parser.add_argument('-r', '--plot-rows', default=1, help='Number of rows in plot')
parser.add_argument('-c', '--plot-cols', default=1, help='Number of columns in plot')
args = parser.parse_args()


# Get the model names
model_names = [f.name for f in os.scandir(args.models_path) if f.is_dir()]


# Create empty dataframe
model_stats = pd.DataFrame(columns=['model', 'acc', 'loss', 'val_acc', 'val_loss'])


# Iterate through each model
for model_name in model_names:
    # Get the model path
    model_path = os.path.join(args.models_path, model_name)

    # Load the model
    learn = load_learner(model_path)

    # Get the model name
    model_name = model_name.replace('_', ' ')

    # Get the model accuracy
    acc = accuracy(learn)

    # Get the model loss
    loss = learn.recorder.losses[-1]

    # Get the model validation accuracy
    val_acc = accuracy(learn.get_model())

    # Get the model validation loss
    val_loss = learn.recorder.losses[-1]

    # Add the model stats to the dataframe
    model_stats = model_stats.append({'model': model_name, 'acc': acc, 'loss': loss, 'val_acc': val_acc, 'val_loss': val_loss}, ignore_index=True)