# Solar-PV
Software Package for visualizing and analyzing efficiency of solar panel modules based on location, efficiency, cost and module tech.

The geocode visualization helps the clients geographically compare the various factors we have analyzed. Color coding, legends and labels will aid the clients in clearly seeing trends across the more than 600,000 cities. Zip code data was converted to Latitude and Longitude, so that it could be numerically compared with the other quantitative data sections such as efficiency and cost. 

Analysis of efficiency with nameplate capacity to give clients an idea of the numerical and statistical correlations. There is first some simple scatter plots to show a basic visualization, and then a regression model fitted. Additional plots are included showing how other factors are uncorrelated. Then a Decision Tree and Simple Neural Network to give some more robust ML analysis. This section of our package is designed for specifically investors, who are most concerned with how well the PV modules work in different places. 

Cost analysis will also take place for purchasers of PV modules. How the module type and location influence the performance will be important, but key factors such as total cost savings compared with correlated factors will tell purchasers what types of PV will be best suited for their locations. 

### Software Dependecies
- Python 3
- geopy
- folium
- sklearn
- keras
- tensorflow



## How To Install





## How To Run
Each Jupyter Notebook will have information for what the code is doing. It is important to download the corresponding py files, which contain functions that the Jupyter Notebook will use while running. 


### Running Tests
Open up the Tests.py file for the corresponding section. 


### Data Info
The data was taken from "The Berkley "Tracking the Sun" Project". We collaboratively parsed down the data and selected the appropriate factors and locations so that we had valid input data. Some locations were repeated and so we cut some to save on computation costs. 

