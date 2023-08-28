import streamlit as st

st.title("Hello Streamlit")

st.header("Header")

st.subheader("Subheader")

st.text("Like this video and subscribe to this channel")

st.markdown("""# h1 tag
## h2 tag
### h3 tag
:moon:<br> 
:laughing:
""",True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')
d ={
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
} 
st.write(d) 


