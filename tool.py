# this is an app the uses streamlit to build an app that does the following:
# 1. loads a dataset
# 2. displays the dataset
# 3. merges the first name and last name columns
# 4. rerrange the data so that unique names each with the corrosponding number of units and units
# 5. display the new dataset

# import libraries
import streamlit as st
import pandas as pd
import numpy as np

st.title("Aira")
st.sidebar.title("Aira")
# allow the user to upload a file
uploaded_file = st.file_uploader("Choose a file")

# 

# if the user uploads a file
if uploaded_file is not None:
    # read the file
    df = pd.read_excel(uploaded_file)
    # display the file
    st.write(df)
    # merge the first name and last name columns
    # check if there is a coumn called first name add last name 
    if 'First Name' in df.columns:
        # merge the first name and last name columns
        df['name'] = df['First Name'] + ' ' + df['Last Name']
        # drop the first name and last name columns
        df.drop(['First Name', 'Last Name'], axis=1, inplace=True)
    else:
        # use column called name
        df['name'] = df['name']
    # drop the first name and last name columns
    # rename Username to units
    
# group the data by name and sum the units in addition the primary phone number and unites
df_count = df.groupby(['name'])['unit number'].count().reset_index()
df_grouped = df.groupby(['name'])['unit number'].sum().reset_index()
df_with_number = df.groupby(['name'])['mobile 1'].first().reset_index()

# merge the dataframes
df = pd.merge(df_count, df_grouped, on='name')
df = pd.merge(df, df_with_number, on='name')
# rename the columns
st.write(df)
df.rename(columns={'unit number_x': 'units', 'unit number_y': 'unit number'}, inplace=True)

# sort by biggest number of units
df.sort_values(by=['unit number'], ascending=False, inplace=True)
# add the units column
# reset the index
df.reset_index(inplace=True)
# display the new dataset
st.markdown("### Final file ###")
st.write(df)

# add download button
st.markdown("### Download File ###")
st.markdown("Download your file here")
# add download button
st.download_button('download', df.to_csv(), 'data.csv')