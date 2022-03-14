import pandas as pd

def import_data(file_path):

    """
    Creates pandas dataframe from .csv in path specified
    Drops nans (nan latitude and longitude columns are excluded)
    Returns pandas dataframe
    :param str file_path: file path of .csv data
    """

    #check that file path is a string
    if not isinstance(file_path, str):
        raise TypeError('File path must be a string.')

    data = pd.read_csv(file_path)
    data = data.dropna() #drops latitude and longitude nans
    return data

def get_eff_average(data):

    """
    Calculates average module efficiency for each state
    Returns pandas dataframe of states and average efficiencies
    :param dataframe-pandas data: dataframe to be plotted
    """
    #test that input is a pandas dataframe
    if not isinstance(data, pd.DataFrame):
        raise TypeError('Input must be a pandas dataframe.')

    #collect unique states
    state_array = data.state.unique()
    #initialize efficiency array
    average_eff = []

    #loop through each state to calculate avg efficiency
    for state in state_array:
        state_df = data[data.state == state]
        avg_eff = state_df['mod_efficiency1'].mean()
        state_df = data[data.state == state]
        average_eff.append(avg_eff)

    #create pandas dataframe
    avg_eff_df = pd.DataFrame({'state': state_array,'avg_eff': average_eff})

    return(avg_eff_df)

def get_reported_costs(file_path):

    """
    Returns a dataframe of only locations with costs reported
    :param str file_path: file path of .csv data
    """
    
    #check that file path is a string
    if not isinstance(file_path, str):
        raise TypeError('File path must be a string.')

    data = pd.read_csv(file_path)
    cost_data = data[data.totalInstalledCost___ != -1]

    return cost_data

def get_cost_average(data):
    
    """
    Calculates average installation cost per module for each state
    Returns pandas dataframe of states and average costs
    :param dataframe-pandas data: dataframe to be plotted
    """
    #test that input is a pandas dataframe
    if not isinstance(data, pd.DataFrame):
        raise TypeError('Input must be a pandas dataframe.')

    #collect unique states
    state_array = data.state.unique()
    #initialize cost array
    average_costs = []

    #loop through states to find average cost per module
    for state in state_array:
        state_df = data[data.state == state]
        avg_cost = state_df['totalInstalledCost___'].mean()
        average_costs.append(avg_cost)

    #create pandas dataframe
    avg_cost_df = pd.DataFrame({'state': state_array,'avg_cost': average_costs})

    return(avg_cost_df)

def get_cost_total(data):

    """
    Calculates total installation costs for all modules for each state
    Returns pandas dataframe of states and total costs in millions of $
    :param dataframe-pandas data: dataframe to be plotted
    """
    #test that input is a pandas dataframe
    if not isinstance(data, pd.DataFrame):
        raise TypeError('Input must be a pandas dataframe.')

    #collect unique states
    state_array = data.state.unique()
    #initialize total cost array
    total_costs = []

    #loop through states to find total cost
    for state in state_array:
        state_df = data[data.state == state]
        total_cost = state_df['totalInstalledCost___'].sum()
        total_costs.append(total_cost/1000000) #use cost in millions

    #create pandas dataframe
    total_cost_df = pd.DataFrame({'state': state_array,'total_cost': total_costs})

    return(total_cost_df)
