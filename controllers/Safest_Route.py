#!/usr/bin/env python
# coding: utf-8

# In[312]:


import numpy as np
import pandas as pd
import sys
import requests
source = [80.22769,13.020528]
destination = [80.254089, 13.096769]
source


# In[314]:


response = requests.get('https://api.mapbox.com/directions/v5/mapbox/driving/' + str(source[0]) + '%2C' + str(source[1]) + '%3B'+ str(destination[0]) + '%2C' + str(destination[1]) + '?alternatives=true&geometries=geojson&language=en&overview=simplified&steps=true&access_token=pk.eyJ1IjoibWF5YW5rNyIsImEiOiJja3Nzdjd2djAwOXpuMnZuc2Roa21jOTE5In0.TBJJunOlHBF2ogW9qWqBBQ')
data = response.json()


# In[315]:


if 'routes' in data and len(data['routes']) > 0:
    # Access route values
    route = data['routes'][0]['geometry']['coordinates']
    print(route)
    


# In[237]:


len(route)


# In[238]:


dataset = pd.read_csv("chennai_crime_scores.csv")


# In[239]:


dataset.head()


# In[240]:


from math import radians, sin, cos, sqrt , atan2


# In[241]:


longitudes = []


# In[242]:


print(route[0:-1])


# In[243]:


lon_values = [lon[0] for lon in route]
print(lon_values)


# In[244]:


longitudes = lon_values
print(longitudes)


# ### We get the latitudes of the first route returned from the api call, we need to do the same for latitudes

# In[245]:


latitudes = []


# In[246]:


lat_values = [lon[1] for lon in route]
print(lat_values)


# In[247]:


latitudes = lat_values
print(latitudes)


# ### We calculate the haversine formula to find the closest areas corresponding this path in the dataset

# In[248]:


map_data = pd.DataFrame({'Latitudes': latitudes, "Longitudes": longitudes})


# In[249]:


map_data.head()


# ### We get the latitudes and longitides in a pandas dataframe

# In[250]:


dataset.head(20)


# In[251]:


dataset_lon = map_data['Longitudes'].to_list()


# In[252]:


print(dataset_lon)


# In[253]:


dataset_lat = map_data['Latitudes'].to_list()


# In[254]:


print(dataset_lat)


# In[255]:


coords_list = [[dataset_lat[i], dataset_lon[i]] for i in range(len(dataset_lat))]


# In[256]:


print(coords_list)


# In[257]:


map_data.head(5)


# In[258]:


def distance(lat1, lon1, lat2, lon2):
    R = 6371  # radius of the Earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

n = 1

# Find the closest coordinates
closest_coords = []
for i in range(0, len(coords_list), 3):
    coords = coords_list[i]
    dists = []
    for j, row in map_data.iterrows():
        dist = distance(coords[0], coords[1], row['Latitudes'], row['Longitudes'])
        dists.append(dist)
    closest = map_data.iloc[np.argsort(dists)[::1][:n]]
    closest_coords.extend(closest[['Latitudes', 'Longitudes']].values.tolist())

print("Closest coordinates:", closest_coords)


# In[259]:


len(closest_coords)


# In[260]:


test_df = pd.DataFrame(closest_coords, columns=['latitude', 'longitude'])


# In[261]:


test_df.head()


# In[263]:


test_df.to_csv('test1.csv', index = False)


# In[264]:


test_df['latitude']= test_df['latitude'].round(2)
test_df['longitude']= test_df['longitude'].round(2)


# In[265]:


test_df.head()


# In[266]:


dataset['latitude']= dataset['latitude'].round(2)
dataset['longitude']= dataset['longitude'].round(2)


# In[267]:


dataset.head()


# In[268]:


similar_values_mask = (abs(dataset['latitude'] - test_df['latitude']) < 0.5) & (abs(dataset['longitude'] - test_df['longitude']) < 0.5)


# In[269]:


similar_values_mask


# In[270]:


similar_values_dataset = dataset[similar_values_mask]
similar_values_test_df = test_df[similar_values_mask]


# In[271]:


similar_values_dataset


# In[272]:


similar_values_test_df


# In[273]:


similar_values_dataset["crime_score"].sum()


# In[274]:


route1_score = similar_values_dataset["crime_score"].sum()
route1_score


# ### We get the crime Aggregate score for the First Path!

# In[275]:


if 'routes' in data and len(data['routes']) > 0:
    # Access route values
    route2 = data['routes'][1]['geometry']['coordinates']
    print(route2)


# ### Now we need to repeat all the steps for the second path as well

# In[276]:


len(route2)


# In[277]:


longitudes2 = []


# In[278]:


lon_values2 = [lon[0] for lon in route2]
print(lon_values2)


# In[279]:


longitudes2 = lon_values2
print(longitudes2)


# ### We get the latitudes of the second route returned from the api call, we need to do the same for latitudes

# In[280]:


latitudes2 = []


# In[281]:


lat_values2 = [lon[1] for lon in route2]
print(lat_values)


# In[282]:


latitudes2 = lat_values2
print(latitudes2)


# ### We calculate the haversine formula again for route 2

# In[283]:


map_data2 = pd.DataFrame({'Latitudes': latitudes2, "Longitudes": longitudes2})


# In[284]:


len(map_data2['Latitudes'])


# In[285]:


map_data2.head()


# In[286]:


dataset.head()


# In[287]:


dataset_lon2 = map_data2['Longitudes'].to_list()


# In[288]:


dataset_lat2 = map_data2['Latitudes'].to_list()


# In[289]:


coords_list2 = [[dataset_lat2[i], dataset_lon2[i]] for i in range(len(dataset_lat2))]


# In[290]:


print(coords_list2)


# In[291]:


if(coords_list == coords_list2):
    print("Yes")
else:
    print("No")


# In[292]:


map_data.head(5)


# In[293]:


# Find the closest coordinates
closest_coords2 = []
for i in range(0, len(coords_list2), 3):
    coords = coords_list2[i]
    dists = []
    for j, row in map_data.iterrows():
        dist = distance(coords[0], coords[1], row['Latitudes'], row['Longitudes'])
        dists.append(dist)
    closest = map_data.iloc[np.argsort(dists)[::1][:n]]
    closest_coords2.extend(closest[['Latitudes', 'Longitudes']].values.tolist())

print("Closest coordinates:", closest_coords2)


# In[294]:


if closest_coords == closest_coords2:
    print("Yes")
else:
    print("No")


# In[295]:


len(closest_coords2)


# In[296]:


test_df2 = pd.DataFrame(closest_coords2, columns=['latitude', 'longitude'])


# In[297]:


test_df2.head()


# In[298]:


test_df2.to_csv('test2.csv', index = False)


# In[299]:


test_df2['latitude']= test_df2['latitude'].round(2)
test_df2['longitude']= test_df2['longitude'].round(2)


# In[300]:


test_df2.head()


# In[301]:


dataset.head()


# In[302]:


similar_values_mask2 = (abs(dataset['latitude'] - test_df2['latitude']) < 0.5) & (abs(dataset['longitude'] - test_df2['longitude']) < 0.5)


# In[303]:


similar_values_mask2


# In[304]:


similar_values_dataset2 = dataset[similar_values_mask2]


# In[305]:


similar_values_dataset2.head()


# In[306]:


similar_values_dataset2['crime_score'].sum()


# In[307]:


route2_score = similar_values_dataset2['crime_score'].sum()
route2_score


# ### We get both our aggregate crime values for the two routes

# In[308]:


if(route2_score > route1_score ):
    print("Route 1 is the safest!")
else:
    print("Route 2 is the safest!")


# ### We need to return the coordinates for the safest path

# In[320]:



# In[321]:




# In[326]:


route1_score


# In[331]:


def return_route(route1_score, route2_score, test_df, test_df2):
    if(route2_score > route1_score ):
        return test_df
    else:
        return test_df2
    


# In[332]:


return_route(route1_score, route2_score, test_df, test_df2)


# In[ ]:




