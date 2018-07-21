import pandas as pd
import numpy as np
from datetime import date, timedelta
import geocoder


def reverse_geocoder(df):
    '''
    get geo data by lat lng via osm API
    '''
    df['geodata'] = ''
    for i in range(len(df)):
        lat = df.lat[i]
        lon = df.lon[i]
        try:
            g = geocoder.osm([lat, lon], method='reverse', timeout=20) #increase timeout if needed
            df.geodata[i] = g.json
            print(i, g.json['country'])
        except (RuntimeError, TypeError, NameError, KeyError):
            pass
    return df


def parse_geodata(df):
    df['country'] = np.nan
    df['country_code'] = np.nan
    df['state'] = np.nan
    df['region'] = np.nan
    df['county'] = np.nan
    df['city'] = np.nan 
    df['district'] = np.nan
    
    for i in range(len(df)):
        g = df.geodata[i]
        try:
            country = g['country']
            country_code = g['country_code']
            df.country[i] = country
            df.country_code[i] = country_code
        except (RuntimeError, TypeError, NameError, KeyError):
            pass

        try:
            state = g['state']
            df.state[i] = state
        except (RuntimeError, TypeError, NameError, KeyError):
            pass

        try:
            region = g['region']
            df.region[i] = region
        except (RuntimeError, TypeError, NameError, KeyError):
            pass
        
        try:
            county = g['county']
            df.county[i] = county
        except (RuntimeError, TypeError, NameError, KeyError):
            pass
        
        try:
            city = g['city']
            df.city[i] = city
        except (RuntimeError, TypeError, NameError, KeyError):
            pass

        try:
            district = g['district']
            df.district[i] = district
        except (RuntimeError, TypeError, NameError, KeyError):
            pass
        
    return df

df = pd.read_csv('data/data.csv')
df = reverse_geocoder(df)
df = parse_geodata(df)
df.to_csv('data/geodata.csv', index=False)