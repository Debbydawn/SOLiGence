import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import altair as alt #pip install altair


data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)


fig, ax = plt.subplots()
plt.scatter(data['a'],data['b'])
plt.title("Scatter Plot")
st. pyplot(fig)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a',y='b',tooltip=['a','b'] # to show value when clicking on a point
)
st.altair_chart(chart,use_container_width= True)

st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share -> watch
watch -> Learn 
Learn -> Utilize

}

""") # flowcharts


# st.bokeh_chart
# st.plotly_chart

city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})


st.map(city)

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)


st.image("image.jpg")

st. audio("demo.wav")

st.video("virtual.mp4")

st.video("https://www.youtube.com/watch?v=9a1NDDcDQ7c")