import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# INITIAL PRESENTATION

st.title('Airbnb in NYC')

# FETCHING THE DATA

DATA = ('data/AB_NYC_2019.csv')

@st.cache_data
def get_data():
  return pd.read_csv(DATA)

data_load_state = st.text('Loading data...')
data = get_data()
data_load_state.text("Data fetching done successfully! (using st.cache_data)")

# SHOWING RAW DATA

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


# HISTOGRAM OF TYPE OF ROOMS

if st.checkbox('Show room types distribution'):
    room_type_counts = data['room_type'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(room_type_counts.index, room_type_counts.values)
    ax.set_xlabel("Room Type")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Room Types")
    plt.xticks(rotation=45)
    st.subheader('Room types')
    st.pyplot(fig)

# MAP

if st.checkbox('Show map'):
    st.subheader(f"Map of NYC Airbnb")
    st.map(data)

# BY NEIGHBOURHOOD

st.title("Airbnb in NYC filter by neighborhood")
selected_neighbourhood = st.sidebar.selectbox("Select Neighborhood", data["neighbourhood"].unique())
filtered_data = data[data["neighbourhood"] == selected_neighbourhood]

# SHOWING RAW DATA IN APP

if st.checkbox(f'Show raw {selected_neighbourhood} data'):
    st.subheader('Raw filtered data')
    st.write(filtered_data)

# HISTOGRAM OF TYPE OF ROOMS

if st.checkbox(f'Show room types distribution in {selected_neighbourhood}'):
    room_type_counts = filtered_data['room_type'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(room_type_counts.index, room_type_counts.values)
    ax.set_xlabel("Room Type")
    ax.set_ylabel("Count")
    ax.set_title(f"Distribution of Room Types in {selected_neighbourhood} neighborhood")
    plt.xticks(rotation=45)
    st.subheader('Room types')
    st.pyplot(fig)


# MAP

if st.checkbox(f'Show map of {selected_neighbourhood}'):
    st.subheader(f"Map of {selected_neighbourhood} neighborhood")
    st.map(filtered_data)



