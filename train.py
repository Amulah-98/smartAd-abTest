from data_info import dataframeInfo
from tree import DecisionTreesModel
from xg import XGBClassifierModel
from logistic_reg import LogesticRegressionModel
from data_visualization import exploration
from data_preProcess import data_preProcess
import sys
import os
import numpy as np
import pandas as pd
import mlflow
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join('..')))
# Adding scripts path
sys.path.insert(0, '../scripts/')


path = 'data/AdSmartABdata.csv'
repo = 'https://github.com/Abel-Blue/smartAd-abTest'


# #Get all train, validate and test sets
browser_v1 = get_train_validate_test_sets(
    browserEncoded-v1['device_make'], predicted_column='response', remove_columns=['auction_id'])

# Train All Models For browser version 1
with mlflow.start_run(experiment_id=1, run_name="browserEncoded-v1"):
    # Logistic Regression Model
    logistic = train_logistic_model(
        browserEncoded-v1['train_x'], browserEncoded-v1['train_y'], browserEncoded-v1['val_x'], browserEncoded-v1['val_y'])

    # Decision Trees
    tree = train_decision_tree(
        browserEncoded-v1['train_x'], browserEncoded-v1['train_y'], browserEncoded-v1['val_x'], browserEncoded-v1['val_y'])

    # XGB Boost
    boost = train_xgb_classifier(
        browserEncoded-v1['train_x'], browserEncoded-v1['train_y'], browserEncoded-v1['val_x'], browserEncoded-v1['val_y'])
