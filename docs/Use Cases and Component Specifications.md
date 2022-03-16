# Use Cases
## Power Companies/Solar Cell Operators
#### User Story
Utility companies that supply power to consumers such as Seattle City Light, ComEd, and DTE are increasingly sourcing their energy from renewable energy sources such as solar cells. Solar cell owners want to ensure their equipment is operating at maximum efficiency to provide the largest amount of power and best return on investment. They want to see which parameters are affecting solar cell efficiency and how they compare to other competitors. These companies employ engineers with the skills needed to understand the various electrical and environmental parameters.

#### Use Case

The Berkley "Tracking the Sun" Project will provide the framework for evaluating which factors affect the efficiency the most. From among the available data tracked, an exploratory data analysis can be created to provide a statistical analysis and data visualization of the factors that most strongly influence the efficiency. Statistical methods such as multiple linear regression, KNN, K-Fold, can be employed. From this broad level result, the power company can have their engineers dive deeper into the inefficiencies of the broad categories the model defines to look for improvements.

## Investor
#### User Story

As solar panels are more widely distributed, business people have to manage the purchasing and installations. They want to use our software to compare the costs of installing solar modules and the net profits from said modules. Investors will want minimal code and just want to select which modules or companies they are interested in, to then compare the data. Their skill level could vary depending on their background. If they’ve been in the solar industry for a while, they might have experience with these kinds of software packages and a general idea of what they are looking for. However, there will inevitably be some who are inexperienced in the solar industry.

#### Use Cases
Users may give information about the company or module they want to see, or want to filter for the data we have available. They will ask for a location to invest in and want mapping of cost and performance. The software should provide specified stats from ML methods (regression, KNN) and mapping. Possible error messages can occur if the investor asks for a company/module/location not in our database.

## Purchaser
#### User Story
Purchasers are those who are looking to install solar panels for their own needs. The PV cells may be installed for residential or public use. They may want to put solar panels on the roof of their homes’, commercial buildings, or public space. The purchasers would want to know about the efficiencies of the solar panels and understand how other factors, such as location and module type, influence the performance. They want to know the predicted cost savings. They will also be concerned with manufacturing and installation costs of each type of PV cell. They are expected to be able to input basic information like location and available square footage. They won’t need any technical knowledge about solar panels. The assumed low skill level of the purchaser impacts the design of the system because the generated information from the system must be conveyed in an easy to understand manner.

#### Use Cases
The purchasers would provide relevant factors, which may include the location and available square footage. The system would provide the best performing company and system in the area. By inputting the square footage, the system would present the efficiency of the module along with the associated costs including installation/maintenance costs and potential savings.

# Component Design

#### 1.  Import Solar Cell Database
  
A parsed down database from the University of California-Berkely “Tracking the Sun” project will be imported into a pandas dataframe. This dataframe will include only the information relevant to the users so that it can be more easily analyzed.

#### 2.  Statistical Analysis
    

1.  Efficiency

	   <ins> Most influential factors on efficiency</ins>: Machine learning algorithms will be employed to determine the factors that most greatly influence the efficiency of the solar cell systems. Algorithms such as multiple linear regression, K-Fold, KNN, and Random Forest can be employed to determine these factors. This information would be provided to the solar cell operating companies so these factors could be looked into more closely by their engineers.

	<ins>Efficiency based on location</ins>: The highest recorded efficiency in the area would be determined along with the company name and module type. The inputs would be location (state, zip code). The code would loop through the code to find data within the same zip code, if it exists, or in the state. The highest efficiency in the area would be determined and outputted along with the corresponding company and module type. This information would be useful to the purchaser and investor users.

    This component enables engineers working for power companies and installers to make informed decisons on which factors most greatly affect efficiency so as to determine which areas they should focus on in deployment of solar cell systems.

2.  Cost analysis
    This provides a brief overview of the associated expenses and income with implementing solar panels. The inputs would include the area (state/zip code) and available square footage. It would find the highest efficiency in the location and use that to calculate the estimated amount of electricity generation based on the approximate number of solar panels that would fit into the entered square footage. Using the average cost of electricity, the potential savings can be calculated. The manufacturing cost per square foot can be calculated by dividing the associated manufacturing cost with the highest efficiency in the area by the number of modules (or sq ft) and then multiplying by the inputted square footage (or number of modules). The outputs would be the predicted manufacturing/installation costs and the potential savings.

    This use case if useful for all users who have some knowledge of python code or can use another employee to help them enalyze cost. The cost analysis will allow installers and power companies to make informed decisions on which systems have lower costs and which areas to focus on to lower cost and maintain sufficient performance.

#### 3.  Visualizations
   The visualization package consits of two components: Geocoding and Map Plotting

   1. Geocoding:
   In order to plot the locations in the dataset, the city and state locations need to be converted to latitude and longitude coordinates. This program takes the entire Tracking the dataframe as an input which includes most importantly for this program, the city and state location of each datapoint. It uses a combinations of a custom python package, Geopy, and Nominatim to output a new dataframe with latitude and longitude in sepearte columns for each datapoint. A jupyter notebook walks the user through how to complete the geocoding. This makes plotting viusualizations in the next step possible.

   2. Map Plotting
   A jupyter notebook is provided to the user to teach them how to plot visualizations using a sample dataset. This component takes a .csv file from the Tracking the Sun dataset as an input and outputs density heat maps and chropleth maps related to cost and efficiency. 

   The visualizations in included in the jupyter notebook are most useful for users with limited to knowledge of python to get an overall idea of the costs and efficiencies based on geographic areas of the United States. This is helpful for the investor to decide which areas would be the best to invest in based areas with high efficiencies, low cost, and potential for expansion.
