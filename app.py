# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:58:50 2023

@author: debna
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("csv_data.csv")

# Split hotel names to extract 'Hotel LA' portion
df['Hotel_Name'] = df['Hotel_Name'].str.split('(').str[0].str.strip()

# Iterate over each star category
for star_category in ['1 Star', '2 Star', '3 Star', '4 Star', '5 Star']:
    # Filter data for the current star category
    star_category_data = df[df['Category'] == star_category]
    
    # Get the top 10 hotel names for the current star category
    top_10_hotels = star_category_data['Hotel_Name'].value_counts().head(10)
    
    # Display the top hotel names for the current star category
    st.write(f"Top 10 hotel names for {star_category}:")
    st.write(top_10_hotels)
    st.write()
    
    # Create a bar plot for the top hotel names
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(top_10_hotels.index, top_10_hotels.values)
    ax.set_title(f"Top 10 Hotel Names for {star_category}")
    ax.set_xlabel("Hotel_Name")
    ax.set_ylabel("Count")
    ax.tick_params(axis='x', rotation=90)
    
    # Display the plot using Streamlit
    st.pyplot(fig)

# Group the data by star category and hotel name, and count the occurrences
star_category_hotel_counts = df.groupby(['Category', 'Hotel_Name']).size().reset_index(name='Count')

# Sort the counts in descending order within each star category
star_category_hotel_counts_sorted = star_category_hotel_counts.sort_values(['Category', 'Count'], ascending=[True, False])

# Get unique star categories
star_categories = star_category_hotel_counts_sorted['Category'].unique()

# Create subplots for each star category
for star_category in star_categories:
    # Filter data for the current star category
    star_category_data = star_category_hotel_counts_sorted[star_category_hotel_counts_sorted['Category'] == star_category]
    
    # Get the top 10 hotel names for the current star category
    top_10_hotels = star_category_data.head(10)
    
    # Create a bar plot for the top hotel names in the current star category
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(top_10_hotels['Hotel_Name'], top_10_hotels['Count'])
    ax.set_title(f"Top 10 Hotel Names for {star_category}")
    ax.set_xlabel("Hotel Name")
    ax.set_ylabel("Count")
    ax.tick_params(axis='x', rotation=90)
    
    # Display the plot using Streamlit
    st.pyplot(fig)

# Filter data for the '4 Star' category
four_star_data = df[df['Category'] == '4 Star']

# Get the top 10 hotel names for the '4 Star' category
top_10_hotels = four_star_data['Hotel_Name'].value_counts().head(10)

# Create a bar plot for the top 10 hotel names in the '4 Star' category
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(top_10_hotels.index, top_10_hotels.values)
ax.set_title("Top 10 Hotel Names for 4 Star")
ax.set_xlabel("Hotel Name")
ax.set_ylabel("Count")
ax.tick_params(axis='x', rotation=90)

# Display the plot using Streamlit
st.pyplot(fig)

# Group the data by 'Hotel Name' and calculate the sum of 'Total Rooms'
total_rooms_per_hotel = df.groupby('Hotel_Name')['Total_Rooms'].sum()

# Sort the data in descending order of total rooms
total_rooms_per_hotel_sorted = total_rooms_per_hotel.sort_values(ascending=False)

# Get the top 10 hotel names with the highest total rooms
top_10_hotels = total_rooms_per_hotel_sorted.head(10)

# Create a bar plot for the total rooms per hotel
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(top_10_hotels.index, top_10_hotels.values)
ax.set_title('Total Rooms per Hotel')
ax.set_xlabel('Hotel Name')
ax.set_ylabel('Total Rooms')
ax.tick_params(axis='x', rotation=90)

# Display the plot using Streamlit
st.pyplot(fig)

# Group the data by 'Hotel Name' and calculate the sum of 'Total Rooms'
total_rooms_per_hotel = df.groupby('City')['Total_Rooms'].sum()

# Sort the data in descending order of total rooms
total_rooms_per_hotel_sorted = total_rooms_per_hotel.sort_values(ascending=False)

# Get the top 10 hotel names with the highest total rooms
top_10_hotels = total_rooms_per_hotel_sorted.head(10)

# Create a bar plot for the total rooms per hotel
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(top_10_hotels.index, top_10_hotels.values)
ax.set_title('Total Rooms per Hotel')
ax.set_xlabel('Hotel Name')
ax.set_ylabel('Total Rooms')
ax.tick_params(axis='x', rotation=90)

# Display the plot using Streamlit
st.pyplot(fig)

# Pie chart of hotel count by category
fig, ax = plt.subplots(figsize=(8, 8))
df['Category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
ax.set_title('Hotel Count by Category')
ax.set_ylabel('')

# Display the plot using Streamlit
st.pyplot(fig)


















































