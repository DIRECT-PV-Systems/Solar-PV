import sklearn         
from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split       
import pandas as pd
import numpy as np

from sklearn.utils import resample
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
from sklearn.feature_selection import f_regression, SequentialFeatureSelector
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

from sklearn.preprocessing import StandardScaler

from sklearn.feature_selection import f_regression, SequentialFeatureSelector

import keras
from tensorflow.keras import Sequential
#from keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import activations
from keras.wrappers.scikit_learn import KerasRegressor
import tensorflow

def simple_network():
    """ Simple Neural Net method, where the type of Net and number of layers are identified."""
    model = Sequential()
    model.add(Dense(7, activation = 'relu', kernel_initializer = 'normal'))
    model.add(Dense(40, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer= 'normal'))
    model.compile(loss = 'mean_squared_error', optimizer = 'adam')
    return model


def keras_regressor(epochs, batch_size, X_train, y_train):
    """ Neural Net Keras regressor. Input the desired number of Epochs and Batch size for the data set. """
    np.random.seed(98)
    estimator = KerasRegressor(build_fn=simple_network,
                              epochs = epochs, batch_size= batch_size, verbose =0)
    history = estimator.fit(X_train, y_train, validation_split=0.33, epochs =epochs,
                           batch_size= batch_size, verbose =1)
    return history


def DecisionTreeRegressor(X_train, X_test, y_train, y_test, y_pred):
    """ A Decision Tree Regressor function that takes in the split X and y, train and test sets, and then calculate r-squared and mean standard deviation """
    dftree =  sklearn.tree.DecisionTreeRegressor().fit(X_train, y_train)
    y_pred = dftree.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print('r2 value:', r2)
    MSE = mean_squared_error(y_test, y_pred)
    print('MSE Value : ', MSE)
    return

def LinearRegressor(X_train, y_train, X_test):
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    Y_calc_test = regr.predict(X_test)
    return