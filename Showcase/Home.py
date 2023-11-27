import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width= 200)

with col2:
    st.title("João Moreira")
    content = """
    Hi, im João! I'm a junior fullstack programmer that has been learning programming for almost a year. I have been 
    learning to program in Java, JavaScript and Python and this will be a little personal webapp where I will show my 
    Python projects... maybe in the future I'll had all my other projects only time will tell...
    """

    st.info(content)

text = """
Below you can find some of the Python apps i have built!
"""
st.write(text)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
