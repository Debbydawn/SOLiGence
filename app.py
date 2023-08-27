import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np 
# import mplcursors

data = pd.read_csv("Salary_Data.csv")
x = np.array(data['YearsExperience']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data['Salary']))


st.title("Salary Predictor")

Nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribution"])

if Nav == "Home":
    st.image("sal.jpg",width = 700)
    # st.write("Home")
    if st.checkbox("Show Table"):
        st.table(data)
    
    val = st.slider("Filter data using years",0,20)
    data = data.loc[data["YearsExperience"] >= val]
    
    graph = st.selectbox("What kind of Graph ? ",["Non-Interactive","Interactive"])
    if graph == "Non-Interactive":
        fig, ax = plt.subplots(figsize=(10, 5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot(fig)
        # # Use mplcursors to add interactive labels
        # mplcursors.cursor(hover=True).connect(
        #     "add", lambda sel: sel.annotation.set_text(f"X: {sel.target[0]:.2f}, Y: {sel.target[1]:.2f}")
        # )

 
    if graph == "Interactive":
        layout = go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range =[0,2100000])
        )
        fig_1 = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode='markers'),layout = layout)
        st.plotly_chart(fig_1)
    
if Nav == "Prediction":
    st.header("Know your Salary")
    val = st.number_input("Enter your year of Experience", 0.00,20.00,step = 0.5)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]
    
    if st.button("predict"):
        st.success(f"Your predicted Salary is {round(pred)}")

if Nav == "Contribution":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your number of Experience years ",0.00,20.00,step = 0.5)
    sal = st.number_input("Enter your Salary Amount", 0.00,1000000.00, step = 1000.00)
    if st.button("Submit"):
        to_add = {"YearsExperience": ex, "Salary": sal}
        
        # Convert the data to a DataFrame
        to_add = pd.DataFrame([to_add])
        
        # Append the data to a CSV file
        to_add.to_csv("Salary_Data.csv", mode='a', header=False, index=False)
        
        st.success("Submitted")
        
        
       