import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

def knn_wrap(df_train, n_neighbors, df_test):
    """
Wrapping function for KNN algorithm

Calls functions functions that perform algorithm

Important assumption: assumes the first two columns are the
training parameters and that the last column is the target vector

Returns predicted values of testing dataframe

:param dataframe-pandas df_train: training dataframe
:param index-integer n_neighbors: number of nearest neighbors
:param dataframe-pandas df_test: testing dataframe
"""


    # test if train and test inputs are pandas dataframes
    if not isinstance(df_train, pd.DataFrame):
        raise TypeError('Train input must be of type: Pandas DataFrame')

    if not isinstance(df_test, pd.DataFrame):
        raise TypeError('Test input must be of type: Pandas DataFrame')

    # test if k inputs are integers
    if not isinstance(n_neighbors, int):
        raise TypeError('n_neighbors input must be of type: Integer')

    # create train and test dataframe subsets
    X_train = df_train.iloc[:, :2]
    y_train = df_train.iloc[:, -1:]

    X_test = df_test.iloc[:, :2]

    # initialize prediction collector
    y_predict = []

    # iterate over X_test to get knn prediction dataframes
    for x_test_index, x_test_row in X_test.iterrows():
        # get sorted list of distances between each X_test point and every x_train point
        df_knn = get_sorted_list(x_test_row.values, X_train, y_train, n_neighbors)

        # make classification prediction
        prediction = predict(df_knn, y_train)

        # add to prediction list
        y_predict.append(prediction)

    # make prediction a pandas dataframe so it's easier to work with
    y_predict = pd.DataFrame(y_predict, index=X_test.index)

    return y_predict


def get_euclidean_distance(x_test_row, x_train_row):
    """
Calculates Euclidean distance between two rows
Returns the distance
:param series-pandas x_test_row: row of pandas dataframe
:param array-numpy x_train_row: row of numpy array
"""

    # calculate euclidean distance between the two input rows
    distance = np.sqrt(np.sum(np.square(x_test_row - x_train_row)))

    return distance


def get_sorted_list(x_test_row, X_train, y_train, n_neighbors):
    """
Sorts list of distances
Returns sorted list of the number of closest
distances defined by n_neighbors
:param array-numpy x_test_row: row of pandas dataframe
:param dataframe-pandas X_train: training dataframe
:param dataframe-pandas y_train: target training dataframe
:param index-integer n_neighbors: number of nearest neighbors
"""

    # initialize distance list
    distance_list = []

    for x_train_index, x_train_row in X_train.iterrows():
        # call distance function to get distance between two rows
        distance = (get_euclidean_distance(x_test_row, x_train_row))

        # add distance to distance list
        distance_list.append(distance)

    # make a list/dataframe for all the distances in this iteration
    df_dists = pd.DataFrame(data=distance_list, columns=['distance'],
                            index=y_train.index)

    # sort the distances in this iteration
    df_knn = df_dists.sort_values(by=['distance'], axis=0)[:n_neighbors]

    # add the corresponding y_train index to the dataframe
    df_knn['y_train_index'] = df_knn.index

    return df_knn


def predict(knn_list, y_train):
    """
Makes classification prediction
Returns class prediction based on the mode of the sorted list
:param dataframe-pandas knn_list: sorted list of neighbors
:param dataframe-pandas y_train: training dataframe
"""
    if 'y_train_index' not in knn_list.columns:
        raise ValueError('y_train indexes must be present')

    # initialize list of y_train values
    y_train_values = []

    # add all y_train values to the list based on the index
    for index in knn_list['y_train_index']:
        y_train_values.append(y_train.loc[index].values[0])

    # create column of y_train values in dataframe
    knn_list['y_train'] = y_train_values

    # find the mode of the y_train values

    if len(knn_list['y_train'].mode()) == 1:

        # if only one mode, prediction is the singular mode
        prediction = knn_list['y_train'].mode().iloc[0]

    else:

        # If there is more than one mode a tie breaker is performed
        prediction = tie_breaker(knn_list)

    return prediction


def tie_breaker(knn_list):
    """
Breaks tie between two modes
The class set with the smallest total euclidean distance wins
Returns class prediction
:param dataframe-pandas knn_list: sorted list of neighbors
"""
    # get list of modes
    mode_list = knn_list['y_train'].mode()

    # check that only lists with multiple modes are being passed
    if len(mode_list) < 2:
        raise ValueError('Only one mode exists')

    mode_list = mode_list.values

    # initialize distance list to hold total distance of mode sets
    distance_list = []

    # iterate over number of modes
    for i in range(len(mode_list)):

        j = 0
        # initialize list to hold euclidean distances
        distances = []

        # iterate over each y_train value
        for y_train_value in knn_list['y_train']:

            # find mode sets
            if mode_list[i] == y_train_value:

                # create list of distances for the mode
                distances.append(knn_list['distance'].iloc[j])

                j += 1

            else:

                j += 1
                continue

        # some distances of one set of modes to the point
        total_distance = sum(distances)

        # add total distance to distance list
        distance_list.append(total_distance)

        # create dataframe of mode distances
    distance_df = pd.DataFrame(data=distance_list, index=mode_list)

    # prediction is mode set with smallest total distance to point
    prediction = distance_df.idxmin().iloc[0]

    return prediction


def k_selection(df_train, df_test, k_list):
    """
Wrapping function for optimal k value from a list

Calls functions that perform algorithm knn algorithm

Important assumption: assumes the first two columns are the
training parameters and that the last column is the target vector

Returns dictionary of accuracy values for each k in the list

:param dataframe-pandas df_train: training dataframe
:param dataframe-pandas df_test: testing dataframe
:param list-integer k_list: list of k values

"""
    # test if k inputs are integers
    for k in k_list:
        if not isinstance(k, int):
            raise TypeError('k inputs must be integers')

    # create train and test dataframe subsets
    X_train = df_train.iloc[:, :2]
    y_train = df_train.iloc[:, -1:]

    X_test = df_test.iloc[:, :2]
    y_test = df_test.iloc[:, -1:]

    # initialize dictionary to store accuracy for each k
    accuracy_dict = {}

    # iterate of k values
    for k in k_list:

        # initialize list to hold predictions
        y_predict = []

        # iterate over X_test to get knn prediction dataframes
        for x_test_index, x_test_row in X_test.iterrows():
            # get sorted list of distances between each X_test point and every x_train point
            df_knn = get_sorted_list(x_test_row.values, X_train, y_train, k)

            # make prediction on each knn set
            prediction = predict(df_knn, y_train)

            # add to prediction list
            y_predict.append(prediction)

        # make prediction a pandas dataframe so it's easier to work with
        y_predict = pd.DataFrame(y_predict, index=X_test.index)

        # get accuracy of of y_predict
        accuracy = accuracy_score(y_predict, y_test)

        # add accuracy/k key to dictionary
        accuracy_dict[k] = accuracy

    # calculate max accuracy
    max_value = max(accuracy_dict.values())

    # print statement to make finding the max accuracy even easier
    print('The optimal k value for this dataset from the list provided is: ',
          {key for key, value in accuracy_dict.items() if value == max_value})

    return accuracy_dict


    






