import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
if st.button('welcome to our page'):
    st.write(' hello')
else:
    st.write('Goodbye')
sreen = st.sidebar.selectbox("select the page:",["page1","page2","page3"])
air_traffic = pd.read_csv('air_traffic_data.csv')
if sreen == "page1":
       st.title('Air Traffic Application')
       st.text('San Francisco International Airport Report on Monthly Passenger Traffic Statistics by Airline')
       air_traffic = pd.read_csv('air_traffic_data.csv')
       air_traffic
acti = st.selectbox("Select Operating Airline",air_traffic['Operating Airline'].unique())
st.write(acti)
plot_type=st.radio("select the plot type",['scatter','line'])
if plot_type =='scatter':
  pl = alt.Chart(air_traffic[air_traffic['Operating Airline']==acti]).mark_circle().encode(
    x = 'Passenger Count',
    y ='Year',
    tooltip = ['Passenger Count','Year']
).interactive()
else:
      pl = alt.Chart(air_traffic[air_traffic['Operating Airline']==acti]).mark_line().encode(
    x = 'Passenger Count',
    y ='Year',
    tooltip = ['Passenger Count','Year']
).interactive()
st.altair_chart(pl)
