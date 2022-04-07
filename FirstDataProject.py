#!/usr/bin/env python
# coding: utf-8

# # My First Data Science Project

# ## Helicopter Escapes!

# We begin by importing some helper functions

# In[2]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'


# In[4]:


data = data_from_url(url)


# Let's print the first three rows

# In[5]:


for row in data: 
    print(data[:3])


# In[6]:


index = 0
for row in data:
    data[index] = row[:-1]
    index += 1

print(data[:3])


# In[7]:


for row in data:
    row[0] = fetch_year(row[0])
    
print(data[:2])


# In[8]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# In[9]:


years = []
for y in range(min_year, max_year + 1):
    years.append(y)


# In[10]:


print(years)


# In[11]:


attempts_per_year = [] 
for y in years: 
    attempts_per_year.append([y, 0])


# In[12]:


for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        if row[0] == y:
            ya[1] += 1
            
print(attempts_per_year) 


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[14]:


countries_frequency = df["Country"].value_counts()


# In[15]:


print_pretty_table(countries_frequency)


# In[ ]:




