#!/usr/bin/env python
# coding: utf-8

# INVESTIGATE A DATASET
# 
# Tmdb_Movie Data
# 
# INTRODUCTION:
# 
# This project will be analysis dataset based on the movies and thier budgets with the revenues generated,genre,year of released,with each movie rating and voting

# QUESTIONS TO ASK THE DATASET
# 
# 
# 1. Which director directed higher number of movie
# 2. Is movie popularity has to do with it profit generated
# 3. let us check relationship between revenue_adj and budget_adj
# 4. Which year has highest movies released
# 5. Which movie generated highest number of revenue
# 

# In[1]:


#importing neccessary libraries like pandas, matplotlib and seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# DATA WRANGLING
# 
# In this section of the report, I will load in the data, check for cleanliness, and then trim and clean the dataset for analysis. Make sure that I document data cleaning steps in mark-down cells precisely and justify cleaning decisions.

# In[2]:


# let load the dataset

data = pd.read_csv('movies.csv')


# In[3]:


#check the numbers of rows and columns of the dataset
data.shape


# In[4]:


#let us check out the dataset

data.head(2)


# In[5]:


# check the information about the data types of each columns
data.info()


# From the look of the dataset the dataset is not proper for analysis, needs some touch of cleaning.
# 
# 
# CLEANING POINTS
# . Drop empty rows
# . Change realise_date column from object to datetime
# . Drop some of irrelevant columns

# In[6]:


#to check for the total of duplicates in the dataset
data.duplicated().sum()


# In[7]:


#let remove the duplicate
data.drop_duplicates()


# In[8]:


# dropping some unneccessary columns which are not useful in analysis, for this let create a function for it.
def drop_cols_rows(dframe, cols_rows, axis):
    dframe.drop(cols_rows, axis=axis, inplace=True)


# In[9]:


columns = ['id', 'imdb_id', 'homepage', 'tagline' ,'keywords', 'overview']

drop_cols_rows(data, columns, 1)


# In[10]:


# let check if the function works as wanted
data.info()


# Yes the function works perfectectly, let proceed
# 

# In[11]:


# next is to drop the null rows using the same function created early
dir_mis = data[data.director.isnull()].index

drop_cols_rows(data, dir_mis, 0)

# I used 0 here because it is rows that I want to drop, unlike early that I used 1 since itwas columns


# In[12]:


data.info()


# Looking at the dataset the genre column needs to be split

# In[13]:


# splitting the column 'genre' into two

data[['movie_kind', 'other']] = data['genres'].str.split('|', n=1, expand=True)


# In[14]:


# let check the dataset

data.info()


# Yes the it works, it has split the column into two columns movie_kind and other

# In[15]:


# I don't need the genre and other columns again in the dataset, the best is to delete them using the function created early

columns  = ['genres', 'other']

drop_cols_rows(data, columns, 1)


# In[16]:


# next is to change the datatype of release_date column


data['release_date'] = pd.to_datetime(data['release_date'])


# In[17]:


data.info()


# Now that the dataset is clean the next step is DATA EXPLORATION

# 
# QEUSTION 1 :
# 
# Which director directed higher number of movies
# 
# 

# In[18]:


data.groupby('director')['original_title'].count().sort_values(ascending=False).head()


# In[31]:


# let vizualize this

data.groupby('director')['original_title'].count().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title('director vs number of movies', fontsize=15)
plt.xlabel('director', fontsize =15)
plt.ylabel('number of movies', fontsize=15);


#  QUESTION 2:
#  
#  Is movie popularity has to do with it profit generated

# In[20]:


# first let create profit column for the dataset
data['profit'] = data['revenue_adj'] - data['budget_adj']


# In[ ]:





# In[30]:


# let create viz between profit and popularity by creating a function


def equation(dframe, x, y, title, xlabel, ylabel):
    sns.regplot(data=dframe, x=x, y=y)
    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.xlabel(xlabel, fontsize=16)
    
equation(data, 'popularity', 'profit', 'Profit Vs Popuplarity', 'Popularity', 'Profit')


# QUESTION 3:
# 
# let us check relationship between revenue_adj and budget_adj

# In[22]:


# I am going to use the above function EQUATION

equation(data, 'revenue_adj', 'budget_adj', 'Revenue_adj Vs Budget_adj', 'Revenue_adj', 'Budget_adj')


# The graph shows that as Budget_adj is increasing the revenue_adj is also increasing

# QUESTION 4:
# 
# Which year has highest movies released

# In[29]:


# let make viz for the year with the highest number of movies released

plt.figure(figsize=[12,10])
data['release_year'].value_counts().plot(kind='bar')
plt.xlabel('release_date', fontsize=16)
plt.ylabel('number of movies', fontsize= 16)
plt.title('release_year vs number of movies', fontsize=20);


# From the graph above, we can deduce that 2014 is the year with the highest number of movie releases

# QUESTION 5:
# 
# Which movie generated highest number of revenue

# In[24]:


#let sort the dataset by the revenue generated in descending order
data.sort_values(by='revenue', ascending=False)


# From above frame it shows that Avater has the highest number of revenue, while Manos:The Hands of Fate has lowest revenue generated generated

# In[25]:


data[data['profit'] == data['profit'].max()]['original_title']


# CONCLUSION:
# 
# 
# 1. Star Wars is the movie with highest profit 
# 2. Avater generated the highest revenue 
# 3. 2014 was the year movies were released most number going to 700 movies
# 4. Director Wooden Allen directed highest number of movies 
# 5. The relationship between the popularity and profit is linear.

# LIMITATION:
# 
# 
# The dataset last released_year was 2014 which shows that,it limts our findings to yer 2014. many movies have been released since then so we need update

# For the completion of this project I made used of Udacity classroom lecture which I followed painstainkly, also I consult some text also sought help from some youtube channels.

# 
