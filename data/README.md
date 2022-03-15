# *Tracking the Sun* data

Berkeley Lab's *Tracking the Sun* report provides data on grid-connected solar photovoltaic (PV) systems throughout the U.S. The report can be accessed [here](https://emp.lbl.gov/tracking-the-sun).


The provided data contains information about over 2 million solar PV projects. The data can be accessed through the link above or [here](https://emp.lbl.gov/sites/default/files/lbnl_publicdatafile_dpv_2021_update_jan2022update.zip). Please note that the data was divided into two files due to large amount of data.

Because the filesize of datasets found from the *Tracking the Sun* report were very large, the csv files of the datasets were combined since they reported the same features for the solar PV projects. Then, the dataset was parsed down since many columns were largely missing data, which was indicated by -1. The percentage of reported data to total in a given column was determined and then columns with insufficient data were removed. Insufficient data was considered to be less than 20%. After this was done, the projects that did not report efficiency values for the solar PV module(s) were then eliminated from the resulting dataset. 

A sample subset 'TTS_sample.csv' of this dataset is provided in this directory so the user can get a basic understanding of the software provided.
