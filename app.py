import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from data_chat import show_data_chat
import yaml

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore", "Chat"))

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
else:
    show_data_chat()