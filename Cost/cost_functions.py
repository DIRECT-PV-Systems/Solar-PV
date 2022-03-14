import pandas as pd
import sklearn

from sklearn.feature_selection import SequentialFeatureSelector

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

# Regressors

# Random Forest Regressor
def random_forest_reg(X_train, y_train, X_test, y_test):
    clf_RF = RandomForestRegressor(n_estimators = 100, max_depth = 4, max_features = 2, random_state = 7)
    clf_RF = clf_RF.fit(X_train, y_train)
    y_predict = clf_RF.predict(X_test)
    mse_RF = mean_squared_error(y_test, y_predict)
    r2_RF = r2_score(y_test, y_predict)
    print(mse_RF)
    print(r2_RF)
    return r2_RF

# Gradient Boosting Regressor
def gradient_boosting_reg(X_train, y_train, X_test, y_test):
    clf_GB = GradientBoostingRegressor(n_estimators=1000, learning_rate=0.1, max_depth=1, random_state=7)
    clf_GB = clf_GB.fit(X_train, y_train)
    y_predict = clf_GB.predict(X_test)
    mse_GB = mean_squared_error(y_test, y_predict)
    r2_GB = r2_score(y_test, y_predict)
    print(mse_GB)
    print(r2_GB)
    
    return r2_GB
    
# Bagging Regressor
def bagging_reg():
    estimator = DecisionTreeRegressor(max_depth=4)
    clf_bag = BaggingRegressor(base_estimator=estimator, n_estimators=100, random_state=7)
    clf_bag = clf_bag.fit(X_train, y_train)
    y_predict = clf_bag.predict(X_test)
    mse_bag = mean_squared_error(y_test, y_predict)
    r2_bag = r2_score(y_test, y_predict)
    print(mse_bag)
    print(r2_bag)
    
    return r2_bag
