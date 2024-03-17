import streamlit as st
import pandas as pd

# Function to create a form
def create_form():
    st.title('Data Entry Form')

    # Input fields
    name = st.text_input('Name')
    surname = st.text_input('Surname')
    age = st.number_input('Age', min_value=0, max_value=150)
    email = st.text_input('Email')
    employed = st.radio('Employed', ['Yes', 'No'])

    if employed == 'Yes':
        salary = st.number_input('Salary', value=0, step=1000)
    else:
        salary = None

    # Check if required fields are filled
    if not (name and surname and age and email):
        st.warning('Please fill in all required fields.')
        return

    # IPL team selection
    st.subheader('IPL Team Support')
    team = st.selectbox('Select your favorite IPL team', [
        'Chennai Super Kings', 'Delhi Capitals', 'Kolkata Knight Riders',
        'Mumbai Indians', 'Punjab Kings', 'Rajasthan Royals',
        'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Other'
    ])

    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    education_level = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master', 'PhD'])
    date_of_birth = st.date_input('Date of Birth')
    nationality = st.text_input('Nationality')
    address = st.text_area('Address')
    phone_number = st.text_input('Phone Number')

    # Submit button
    if st.button('Submit'):
        data = {
            'Name': name,
            'Surname': surname,
            'Age': age,
            'Email': email,
            'Employed': employed,
            'Salary': salary,
            'Favorite IPL Team': team,
            'Gender': gender,
            'Education Level': education_level,
            'Date of Birth': date_of_birth,
            'Nationality': nationality,
            'Address': address,
            'Phone Number': phone_number
        }
        # Store data in Excel
        store_data(data)
        st.success('Data submitte
