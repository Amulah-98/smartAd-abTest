from multiapp import MultiApp
from applications import model, user_engagement, experience_analytics, satisfaction_analysis
import os
import sys
import streamlit as st

sys.path.insert(0, './dashboard')


st.set_page_config(page_title="smartAd-test", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# smartAd-test
""")

# Add all your application here
app.add_app("user_engagement", user_engagement.app)
app.add_app("experience_analytics", experience_analytics.app)
app.add_app("satisfaction_analysis", satisfaction_analysis.app)
app.add_app("Model", model.app)

# The main app
app.run()
