import streamlit as st

st.title("Registration Form")

# first,last = st.beta_columns(2)

columns = st.columns(2)  # Create two columns
first_column = columns[0]
last_column = columns[1]


first_column.text_input("First Name")
last_column.text_input("Last Name")

columns_1 = st.columns([3,1]) # the [3,1] tells it to make the first column 3 times bigger than the second
email_col = columns_1[0]
num_col = columns_1[1]

email_col.text_input("Email Address")
num_col.text_input("Phone Number")

columns_2 = st.columns(3)
user_name = columns_2[0]
password_1 = columns_2[1]
password_2 = columns_2[2]

user_name.text_input("Username")
password_1.text_input("Password",type = "password")
password_2.text_input("Retype your Password",type = "password")

ch,bl,sub = st.columns(3)

with ch:
    st.checkbox("I agree")

with sub:
    st.button("Submit")



