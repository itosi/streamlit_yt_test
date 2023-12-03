#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import sys
# !{sys.executable} -m pip install streamlit


# In[2]:


# import streamlit as st


# In[1]:


# import pandas as pd


# In[ ]:


# get_ipython().system('pip list | findstr streamlit')


# In[ ]:

# Import the necessary libraries

import pandas as pd
# import pyodbc 


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import matplotlib


import os 




# from azure.identity import DefaultAzureCredential

# # Azure AD Authentication
# credential = DefaultAzureCredential()


# server_name = 'mneu-sql-d-dbadvan-001.database.windows.net'
# database_name = 'mneu-db-d-dbadvan-pricing-001'

# # Create the connection string
# connection_string = \
# f"Driver={{ODBC Driver 17 for SQL Server}};\
# Server={server_name};\
# Database={database_name};\
# Authentication=ActiveDirectoryInteractive"

# # Connect to the server
# conn = pyodbc.connect(connection_string, authentication = credential)

# # Create the cursor; an object that is needed, if you want to run SQL queries
# cursor = conn.cursor()
# #print(conn)














import streamlit as st
st.title('My first project!!')
st.subheader('How are you?')
st.text('I am exploring ways to work and use streamlit.')
st.markdown("# [Hi](https://google.com)")
code=''' 
import pandas as pd
import numpy as np
'''
st.code(code)

var=2
st.text(f"the value is {var}.")
var3 = st.text_input('Team:') 


st.write(f'''PWP Sensitivity:

With {var3} 9 0% rough change, and a realized  -3.6% PWP,  S9 Spot RTOP will narrow to 1.28, reduced from last Sight’s 1.33.\n
With S9 0% rough price change and -3.6% PWP change the S09 Lagged RtoP  widens from 1.25 to 1.28  (S6 -6.0% rough, and S9 -3.6% PWP) (next 3 Sights the lagged RtoP change and direction will solely depend on PWP, because S7-S9 rough=0%)
Hypothesis: With S10 0% rough price change and S10 -2.0% PWP change, the S10 (next cycle’s Lagged RtoP!!) Lagged RtoP will narrow from 1.28 today to 1.25  (S7 0.0% rough, and S10 -2% PWP)
To take current  S9 Lagged RtoP of 1.28 to 1.41 you need to drop rough price by -9.3%. Equivalent PWP increase required is +10.2%
With a S9 0% rough price change and -3.6% PWP, the IPC moves from -5.9% to -9.3%
If we assume the LT sustainable RtoP is 1.40 as opposed to 1.41 due to Delta effect.... the current S9 IPC will now be  -8.6% as opposed to -9.3%.''')

