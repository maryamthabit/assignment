import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
air_traffic = pd.read_csv('air_traffic_data.csv')
st.title('Air Traffic Application')
options = st.multiselect('what you think is the GEO Region that has the highest rate over the years?',
    ['US', 'Canada', 'Asia', 'Europe', 'Australia / Oceania', 'Mexico',
       'Central America', 'Middle East', 'South America'])
       
df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)

plot_type=st.checkbox("bar")
plot_typ2=st.checkbox("hist")
if plot_type :
   plt.bar(air_traffic['Year'],air_traffic['GEO Region'])
if plot_typ2:
   plt.hist(air_traffic['GEO Region'],bins=5)
