#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os


# In[6]:


# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Change the directory to a new path
new_directory = 'C:\\Users\\chris\\OneDrive\\Documents\\Data Science Bootcamp\\Module 6 Challenge\\Starter_Code\\output_data\\API Challenge'
os.chdir(new_directory)

# Verify the directory has changed
updated_directory = os.getcwd()
print("Updated working directory:", updated_directory)


# In[1]:


pwd

