import os
import numpy as np
import pandas as pd
import urllib.request
import geocoder
import matplotlib.pyplot as plt
from PIL import Image
from gmplot import gmplot


HK_LOCATION = (22.396400, 114.10950)
    
def geomap(data, zoom=11, point_size=3, point_color='r', point_alpha=1, y=HK_LOCATION[0], x=HK_LOCATION[1]):
    '''
    plot point location on OSM map
    default parameters: zoom into Hong Kong bounding box
    '''
    datadir='map/'
    
    # corrections to match geo with static map
    z = zoom
    picsize=1000
    wx = 1.0*360*(picsize/256)/(2**z) 
    wy = 0.76*360*(picsize/256)/(2**z) 

    x_min, x_max = x-wx/2, x+wx/2
    y_min, y_max = y-wy/2, y+wy/2

    static_map_filename = os.path.join(datadir, 'map_zoom{}.png'.format(z,picsize))
    if os.path.isfile(static_map_filename)==False:
        osm_staticmap_api(x,y,z,picsize,static_map_filename)

    print('OSM map file location: ',static_map_filename)
    img = Image.open(static_map_filename)     

    # add the static map
    plt.imshow(img, zorder=0, extent=[x_min, x_max, y_min, y_max], interpolation='none', aspect='auto')

    # add the scatter plot of events
    plt.plot( 
        data['lon'], 
        data['lat'], 
        '.', 
        markerfacecolor=point_color, 
        markeredgewidth=0.0,
        markersize=point_size, 
        alpha=point_alpha)

    # limit the plot to the given bounding box
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    

def osm_staticmap_api(x,y,z,size,filename) :
    static_map = "http://staticmap.openstreetmap.de/staticmap.php?center={0},{1}&zoom={2}&size={3}x{3}&maptype=mapnik".format(y,x,z,size)
    static_map_filename, headers = urllib.request.urlretrieve(static_map, filename)
    return static_map_filename