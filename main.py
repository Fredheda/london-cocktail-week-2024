import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
import sqlite3
from utils.FoliumClient import add_bar_to_map

conn = sqlite3.connect("LCW.db")

st.set_page_config(layout="wide")
st.title('London Cocktail Week 2024')

bars = pd.read_sql('SELECT * FROM bars', conn)
drinks = pd.read_sql('SELECT * FROM drinks', conn)

with st.sidebar:
    bar_selection = st.multiselect("Select Bar(s)", options=bars['Bar Name'].unique().tolist())

if bar_selection != []:
    bars = bars[bars['Bar Name'].isin(bar_selection)]

map_center = [bars['Latitude'].mean(), bars['Longitude'].mean()]
map = folium.Map(location=map_center, zoom_start=12)

for bar_idx, bar_row in bars.iterrows():
    filtered_drinks = drinks[drinks['Bar ID'] == bar_row['Bar ID']]
    popup = f" Bar: {bar_row['Bar Name']}\n"
    for drink_idx, drink_row in filtered_drinks.iterrows():
        popup += f"Drink: {drink_row['Drink']} Score: {drink_row['Score']} \n\n"
    
    map = add_bar_to_map(map, bar_row, popup, filtered_drinks)
st_data = st_folium(map, width=1400, height=400)