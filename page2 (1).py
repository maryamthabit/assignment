import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
air_traffic = pd.read_csv('air_traffic_data.csv')
st.title('Air Traffic Application')

number = st.number_input('what you Suggest the number of Passenger Count')
st.write('The current number is ', number)
pie_chart = px.pie(air_traffic, 
            title='number of Passenger with the GEO Region',
            values='Passenger Count',
            names='GEO Region')
st.plotly_chart(pie_chart)
