# Geospatial Analysis

This repo presents data visualization of gelocation data, geospatial analysis and clustering algorithm. For illustration purpose, all data presented in this repo are synthesized data only. For deployment, API is called to query data from Redshift database and conduct visualization of geolocation data at specific time point. 

See `demo-geospatial-analysis.ipynb` [Link](https://nbviewer.jupyter.org/github/sukilau/demo-geospatial-analysis/blob/master/demo-geospatial-analysis.ipynb.ipynb)


## Map Visualization of Geolocation Data

To visualize the geolocation data on the map, we have called [OpenStreetMap API](https://wiki.openstreetmap.org/wiki/API) to get the map within the desired bounding box and plot the point locations on the map. 

![hkmap](https://github.com/sukilau/demo-geospatial-analysis/blob/master/plot/hkmap.png)


## K-means Clustering

Clustering algorithms, such as k-means can be used to determine which geographical areas are popular by users. It can be useful to enable location-based services to provide a more personalized user experience. We have filtered the geolocation data to Hong Kong, clustered Hong Kong into 20 geographical areas, and visualized the results using Voronoi diagram.

![kmeans](https://github.com/sukilau/demo-geospatial-analysis/blob/master/plot/kmeans_20clusters.png)