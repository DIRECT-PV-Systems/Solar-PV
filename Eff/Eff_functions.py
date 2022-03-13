def simple_network():
    model = Sequential()
    model.add(Dense(7, activation = 'relu', kernel_initializer = 'normal'))
    model.add(Dense(1, kernel_initializer= 'normal'))
    model.compile(loss = 'mean_squared_error', optimizer = 'adam')
    return model


def keras_regressor(epochs, batch_size):
    """ Neural Net Keras regressor. Input the desired number of Epochs and Batch size for the data set. """
    np.random.seed(98)
    estimator = KerasRegressor(build_fn=simple_network,
                              epochs = epochs, batch_size= batch_size, verbose =0)
    history = estimator.fit(X_train, y_train, validation_split=0.33, epochs =30,
                           batch_size=1000, verbose =1)
    return


def DecisionTreeRegressor(X_train, X_test, y_train, y_test):
    dftree =  sklearn.tree.DecisionTreeRegressor().fit(X_train, y_train)
    y_pred = dftree.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print('r2 value:', r2)
    MSE = mean_squared_error(y_test, y_pred)
    print('MSE Value : ', MSE)