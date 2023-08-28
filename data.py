import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":["Deborah","Promise"],
    "age":[24,25],
    "city":["southam","Ogun"]
}

data =  pd.read_csv("Salary_Data.csv")
# "C:\Users\adedi_tpk1ys1\Streamlit\Salary_Data.csv"
st. dataframe(data,width=100,height= 500)  
st.table(data)
st. table(dic)
st.json(dic)
st.write(nd) # can be used for all forms of datas
# caching mechanism when we mark a function cache decorator it tells the functions that whenever it is been called it should check
# some list, the input parameter called with the function,the value of internal variables used in the function and body of the function
# and lastly, body of any function used inside the cache function.
# so if its sees something it has run it will skip it and give the previous output stored in the cache
@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(1))