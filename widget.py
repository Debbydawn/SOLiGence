import streamlit as st

st.title("WIDGETS")


if st.button("Subscribe"):
    st.write("Like this video too")
    st.audio("demo.wav")
    name = st.text_input("Name")
    st.write(name)
    address = st.text_input("Enter your Address")
    st.write(address)
    email = st.text_input("Enter your E-mail address")
    st. write(email)
    st.date_input("Enter a Date")
    st. time_input("Enter a time avaliable")
# this can also stand on there own

if st.checkbox("You accept the T&C", value=True):
    st.write("Thank You and Welcome")
v1 = st.radio("Colours",["r","g","b"]) # add index = 1 for the default selection
v2 = st.selectbox("Colours",["Red","Green","Blue"],index = 0)

st.write(v1,v2)

v3 = st.multiselect("Colours",["Red","Green","Blue","Purple","Pink","Black"])
st.write(v3)

# st.slider("age")# set the min and max, add step to change the rate of movement defalut is 1
st.slider("age",min_value = 18, max_value = 80, value = 20,step = 3) 
# add .0 to all number to have float numbers
st.number_input("Enter number",min_value = 18.0, max_value = 80.0, value = 20.0,step = 3.0)

file1 = st.file_uploader("Upload a file")
st.image(file1) # you can add a function to check the file and display all types of files



