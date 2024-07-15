# Software Developer Salary Predictor + Gemini LLM
Link: https://onionsp-developer-salary-predictor-app-mdmqve.streamlit.app/

<img src="https://github.com/onionsp/Developer-Salary-Predictor/blob/main/Screenshots/Screenshot%202024-07-14%20at%207.53.49%E2%80%AFPM.png" width="600">
<img src="https://github.com/onionsp/Developer-Salary-Predictor/blob/main/Screenshots/Screenshot%202024-07-14%20at%207.53.59%E2%80%AFPM.png" width="600">
<img src="https://github.com/onionsp/Developer-Salary-Predictor/blob/main/Screenshots/Screenshot%202024-07-14%20at%207.54.06%E2%80%AFPM.png" width="600">


## Description

ML Project that focused on end to end ML pipeline. Used the stackoverflow 2023 developer survey:https://survey.stackoverflow.co
Packaged the ML model into a streamlit app and deployed it on their community platform. 
Finished model classifies roughly within $30,000 of actual salary.

I just added a new chat page which uses PandasAI and google's free Gemini plan to allow users to chat with data. Quite cool use of LLM's. 
PSA the feature can be buggy on web deployment. Clone repo and use your own API key for best results.

## Key Learnings
- Data cleaning on large dataset
- Dealing with outliers
- Importance of understanding data before rushing into models (Garbage in Garbage out)
- How to build + deploy streamlit apps. (found it was quite straightforward but ran into issues with hosting CSV file on github as too large)
- How to connect LLM to PandasAI and deploy on streamlit
- How to hide API keys for security
## Further development plans
- Experiment with using different features to improve predictive accuracy of model
- Explore further uses of LLM for data analysis through natural language
