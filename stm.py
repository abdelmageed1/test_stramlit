import streamlit as st
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('train.csv')


# to edit of page confg
st.set_page_config(page_title='Allam',
                    page_icon=None, 
                    layout="centered",
                      initial_sidebar_state="auto",
                        menu_items=None)


# Sidebar or with 
sidebar = st.sidebar
sidebar.header('Hello World')
sidebar.image('1-.png')
sidebar.write('I am Abedelmageed Fathy AI Engineer')
sidebar.markdown('This my profile :heart_eyes: :[Linked in ](https://www.linkedin.com/in/abdelmageed-fathy-3825861bb/) ')

# filttering in sidebar
st.write()
st.write('select category')
cat_selected = sidebar.selectbox('Category' , ['cut','color','clarity'])



#Body
 
# row 1 
col1, col2, col3 = st.columns(3)
col1.metric("Max Price ",data['price'].max())
col2.metric("Min Price ",data['price'].min())
col3.metric("Mean Price ",np.ceil(data['price'].mean()))

# row 2

c1 ,c2  = st.columns(2)

with c1  :
    fig = px.histogram(data , x='price' ,  histfunc='avg')
    st.plotly_chart(fig ,use_container_width=True)
     # use_container_width to response screen 

with c2  :
    fig = px.bar(data, x="cut", y="price", color= cat_selected, barmode="group")
    st.plotly_chart(fig ,use_container_width=True)


# row 3
st.write('Pie Graph')
fig = px.pie(data, values='price', names='color')
st.plotly_chart(fig ,use_container_width=True)


























