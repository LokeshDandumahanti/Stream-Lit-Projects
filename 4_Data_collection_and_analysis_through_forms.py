import streamlit as st
import pandas as pd
import seaborn as sns

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
        st.success('Data submitted successfully!')

        # Display pie chart for IPL team support
        show_team_support_chart()

# Function to store data in Excel
def store_data(data):
    try:
        existing_df = pd.read_excel('data.xlsx')
        updated_df = pd.concat([existing_df, pd.DataFrame(data, index=[0])], ignore_index=True)
        updated_df.to_excel('data.xlsx', index=False)
    except FileNotFoundError:
        pd.DataFrame(data, index=[0]).to_excel('data.xlsx', index=False)

# Function to show pie chart for IPL team support
def show_team_support_chart():
    try:
        data = pd.read_excel('data.xlsx')
        team_counts = data['Favorite IPL Team'].value_counts()
        plt.figure(figsize=(8, 6))
        sns.set_palette('pastel')
        sns.barplot(x=team_counts.index, y=team_counts.values)
        plt.xticks(rotation=45)
        plt.xlabel('IPL Team')
        plt.ylabel('Number of Supporters')
        plt.title('Number of Supporters for Each IPL Team')
        st.pyplot()
    except FileNotFoundError:
        st.warning('No data submitted yet.')

# Main function
def main():
    create_form()

    # Display stored data
    try:
        stored_data = pd.read_excel('data.xlsx')
        st.title('Stored Data')
        st.write(stored_data)
    except FileNotFoundError:
        st.warning('No data submitted yet.')

if __name__ == "__main__":
    main()
