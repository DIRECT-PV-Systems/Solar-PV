This directory includes a toolkit for visualizing the Tracking the Sun Project data on a map.

The geocoding program and accompanying jupyter notebook walk the user thorugh how to geocode the data set. This is done in order to get precise latitude and longitude locations for each solar cell module. Since the full dataset is too large to store on github, a sample file is provided to show the user how the geocoding works in a reasonable amount of time. The full dataset takes over 3 hours to geocode just the unique cities in the dataset. The results of this are provided for information purposes and can be found in data/from_full_dataset. The files that end in '_full' are from the full dataset and likewise the output files that run in the jupyter notebook from the sample dataset end in '_sample'.

The Visualization jupyter notebook walks the user through visualizing the data on maps plotted with Folium and using the visualization python program. The demos included in the notebook include plotting a heat map of all locations and chropleths related to cost and efficiency. The code for the Folium maps is included in the notebook so that the user can play with the parameters.

To view some of the maps created from the full dataset, see the images in the visualizations/images folder.
