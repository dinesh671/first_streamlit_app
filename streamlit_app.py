import streamlit as s
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

s.title('my_fruit_list')

s.header('Breakfast Menu')
s.text('🥣 Omega 3 & Blueberry Oatmeal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-Boiled Free-Range Egg')
s.text('🥑🍞 Avocada Toast')

s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = s.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
s.dataframe(my_fruit_list)

s.header("Fruityvice Fruit Advice!")

fruit_choice = s.text_input('What fruit would you like information about?','Kiwi')
s.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
s.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**s.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
s.text("Hello from Snowflake:")
s.text(my_data_row)

s.header("The Fruit load list contains:")

# s.datafame(my_fruit_list)
# add_my_fruit = s.text_input('What fruit would you like to add?','jackfruit')
# s.write('Thanks for adding', add_my_fruit)
