import streamlit as st
import requests
import numpy as np
import TextSummarisation as ts
import TextLink as tl
from newspaper import ArticleException

st.title("Text SummariZation Project")
st.sidebar.header("Text Summarisation Format")

with st.sidebar:
    formate=["Text","Link"]
    source=st.radio("Select a Format of text",formate)
        
if(source=="Text"):
    note=st.text_input("Enter The Text:")
    input_note=ts.declare_text(note)
    st.write(input_note)
    summary=ts.summarize(input_note)
    st.caption(":green[SUMMARIZED TEXT:]")
    st.markdown(f":blue[{summary}]", unsafe_allow_html=True)
    
else:
    try:
        url=st.text_input("Enter the URL:")
        input_text=tl.extract_text(url)
        input_notee=ts.declare_text(input_text)
        st.write(input_notee)
        summary=ts.summarize(input_notee)
        st.caption(":green[SUMMARIZED TEXT:]")
        st.markdown(f":blue[{summary}]", unsafe_allow_html=True)        
    except ArticleException as e:
        st.write("***Note:url should starts with https://***")


st.snow()

