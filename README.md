# Solar-PV
Software Package for visualizing and analyzing efficiency of solar panel modules based on location, efficiency, cost and module tech.

The geocode visualization helps the clients geographically compare the various factors we have analyzed. Color coding, legends and labels will aid the clients in clearly seeing trends across the more than 600,000 cities. City and state data were geocoded to latitude and longitude, so that it could be numerically compared with the other quantitative data sections such as efficiency and cost. 

Analysis of efficiency with nameplate capacity to give clients an idea of the numerical and statistical correlations. There is first some simple scatter plots to show a basic visualization, and then a regression model fitted. Additional plots are included showing how other factors are uncorrelated. Then a Decision Tree and Simple Neural Network to give some more robust ML analysis. This section of our package is designed for specifically investors, who are most concerned with how well the PV modules work in different places. 

Cost analysis will also take place for purchasers of PV modules. How the module type and location influence the performance will be important, but key factors such as total cost savings compared with correlated factors will tell purchasers what types of PV will be best suited for their locations.

### Software Dependecies
- Python 3
- geopy
- folium
- sklearn
- keras
- tensorflow

### Data Info
The data was taken from the University of California-Berkley "Tracking the Sun" Project". We collaboratively parsed down the data and selected the appropriate factors and locations so that we had valid input data of a more manageable size. Since efficiency was identified to be on of the most important factors for cost, only the states that reported efficiency data were included in these analyses. This reduced the datapoints from 1.2 million to 600,000. The capacity, size, number of modules, and location columns reported in the dataset become important factors in these analyses.


## How To Install
This repository can be forked or downloaded by the user. Since the full dataset file is too large, the full dataset is not available on GitHub. A sample subset of the data is provided. Please contact the authors if you wish to use the full dataset.

## How To Run
Each Jupyter Notebook in the visualization, efficiency, and cost directories will have information on how to run the analysis software. It is important to download the corresponding .py files, which contain functions that the Jupyter Notebook will use while running. 


### Running Tests
Each directory contains a corresponding 'test' subfolder which contains unittest for each module. 




