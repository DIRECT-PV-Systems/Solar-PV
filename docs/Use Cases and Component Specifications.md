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

2.  Cost analysis
    This provides a brief overview of the associated expenses and income with implementing solar panels. The inputs would include the area (state/zip code) and available square footage. It would find the highest efficiency in the location and use that to calculate the estimated amount of electricity generation based on the approximate number of solar panels that would fit into the entered square footage. Using the average cost of electricity, the potential savings can be calculated. The manufacturing cost per square foot can be calculated by dividing the associated manufacturing cost with the highest efficiency in the area by the number of modules (or sq ft) and then multiplying by the inputted square footage (or number of modules). The outputs would be the predicted manufacturing/installation costs and the potential savings.

#### 3.  Visualizations
   Using a package such as GeoPandas, our software will be able to create maps for easily comparing factors such as efficiencies, companies, module tech, etc. These maps will give Power Companies, Investors and Purchasers the ability to easily view trends, with varying degrees of technical knowledge. This will involve code to create the visualizations with graphical elements to alter specific parts such as labels, markers, color coding, legends.
