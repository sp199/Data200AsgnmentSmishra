#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import streamlit as st
import pandas as pd
df= pd.read_csv('Fish.csv')
fig= px.bar(df, x= 'Spicies', y= 'Weight')
st.plotly_charts(fig)


# In[ ]:




