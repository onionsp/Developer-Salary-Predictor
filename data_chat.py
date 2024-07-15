import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import GoogleGemini

TOKEN = st.secrets["TOKEN"]

def show_data_chat():
    st.write("# Chat with Developer Survey Dataset")

    df = pd.read_csv("./data/survey_results_public.csv")

    with st.expander("🔎 Dataframe Preview"):
        st.write(df.tail(3))

    query = st.text_area("🗣️ Chat with Dataframe using Gemini")
    container = st.container()

    if query:
        llm = GoogleGemini(api_key=TOKEN)
        query_engine = SmartDataframe(
            df,
            config={
                "llm": llm,
            },
        ) 
        answer = query_engine.chat(query)
        st.write(answer)
        