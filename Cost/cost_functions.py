import numpy as np
import pandas as pd
import sklearn

from sklearn import linear_model
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.model_selection import train_test_split


# Stepwise Selection

def forward_stepwise_selection(X, y, f_names):
    sfs_forward = SequentialFeatureSelector(linear_model.LinearRegression(),
                                        n_features_to_select=5,
                                        direction = 'forward').fit(X,y)
    print('support: ', sfs_forward.get_support(), "\n")
    selected = sfs_forward.get_support(indices = True)
    print(selected)
    print('Selected input features using Forward Stepwise Selection: \n', f_names[selected])
    return f_names[selected]

def backward_stepwise_selection(X, y, f_names):
    sfs_backward = SequentialFeatureSelector(linear_model.LinearRegression(),
                                        n_features_to_select=5,
                                        direction = 'backward').fit(X,y)
    print('support: ', sfs_backward.get_support(), "\n")
    selected = sfs_backward.get_support(indices = True)
    print(selected)
    print('Selected input features using Forward Stepwise Selection: \n', f_names[selected])
    return f_names[selected]

def different_values(list1, list2):
    return list(set(list1).symmetric_difference(set(list2)))

def unique_values(list1, list2):
    return list(set(list1) | (set(list2)))


# Random Forest Regressor
def random_forest_reg(X_train, y_train, X_test, y_test):
    clf_RF = RandomForestRegressor(n_estimators = 100, max_depth = 4, max_features = 2, random_state = 7)
    clf_RF = clf_RF.fit(X_train, y_train)
    y_predict = clf_RF.predict(X_test)
    mse_RF = mean_squared_error(y_test, y_predict)
    r2_RF = r2_score(y_test, y_predict)
    print(mse_RF)
    print(r2_RF)
    return r2_RF, y_predict
