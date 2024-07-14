import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.responses.response_parser import ResponseParser

def show_data_chat():
    st.write("# Chat with Developer Survey Dataset")

    df = pd.read_csv("./data/survey_results_public.csv")

    with st.expander("🔎 Dataframe Preview"):
        st.write(df.tail(3))

    query = st.text_area("🗣️ Chat with Dataframe")
    container = st.container()

    if query:
        llm = OpenAI(api_token=os.environ["sk-proj-keRFWakhymVhcc2aNxF0T3BlbkFJvA0ujStFB7yM6gHwwLP3"])
        query_engine = SmartDataframe(
            df,
            config={
                "llm": llm,
            },
        ) 
        answer = query_engine.chat(query)
        st.write(answer)
        