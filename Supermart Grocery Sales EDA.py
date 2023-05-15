#!/usr/bin/env python
# coding: utf-8

# In[81]:


#importing the necessary libraries

import pandas as pd
import numpy as np
import seaborn as sns


# In[82]:


#loading the dataset

df= pd.read_csv('Supermart Grocery Sales - Retail Analytics Dataset.csv')


# In[83]:


df.head()


# In[84]:


#checking the rows and column of the dataset

df.shape


# In[85]:


#checking the data type of each column

df.dtypes


# In[86]:


#check for null or missing values

df.isna().sum()


# In[87]:


#remove unncessary columns 

df=df.drop(columns=['State'])


# In[94]:


#create new year and month column from order date

df['Year'] = pd.DatetimeIndex(df['Order Date']).year
df['Month'] = pd.DatetimeIndex(df['Order Date']).month


# In[95]:


#change the necessary columns to the right dataset

df['Order Date'] = pd.to_datetime(df['Order Date'])


# In[96]:


df.dtypes


# In[99]:


df.describe()


# In[97]:


#save and export the cleaned data to powerBI for visualization

df.to_csv('Supermart_Grocery_Sales_Dataset.csv')


# In[ ]:




