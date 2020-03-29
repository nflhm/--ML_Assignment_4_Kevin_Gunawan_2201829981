#!/usr/bin/env python
# coding: utf-8

# In[101]:


import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import statistics as st
import seaborn as sb
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from scipy.stats import norm
nd = pd.read_csv("listings.csv")
nd['reviews_per_month'].fillna(0, inplace = True)
# print(nd.head())


# In[107]:


# distNd = nd[["price", "minimum_nights", "number_of_reviews", "calculated_host_listings_count", "availability_365", 
#              "latitude", "longitude", "reviews_per_month"]]
# distNd.hist()
# plt.subplots_adjust(hspace = 0.8, wspace = 0.8)
# plt.rcParams["figure.figsize"] = [16,9]
# plt.show()


# In[114]:


plt.subplot(331)
sb.distplot(nd["price"], color="orange")
plt.xlabel("Price")

plt.subplot(332)
sb.distplot(nd["minimum_nights"], color="magenta")
plt.xlabel("Minimum Nights")

plt.subplot(333)
sb.distplot(nd["calculated_host_listings_count"], color="grey")
plt.xlabel("Calculated Host Listings Count")

plt.subplot(334)
sb.distplot(nd["availability_365"], color="green")
plt.xlabel("Availability 365")

plt.subplot(335)
sb.distplot(nd["number_of_reviews"], color="blue")
plt.xlabel("Number of Reviews")

plt.subplot(336)
sb.distplot(nd["latitude"], color="pink")
plt.xlabel("Latitude")

plt.subplot(337)
sb.distplot(nd["longitude"], color="purple")
plt.xlabel("Longitude")

plt.subplot(338)
sb.distplot(nd["reviews_per_month"])
plt.xlabel("Reviews per Month")

plt.rcParams["figure.figsize"] = [20,18]


# In[ ]:




