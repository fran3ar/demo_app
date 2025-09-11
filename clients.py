import streamlit as st
import pandas as pd
from st_db import conn  # SQLConnection de st_db

def load_data(query):
    result = conn.query(query)
    return pd.DataFrame(result)

def app():
    st.subheader("📊 Clients")

    # load data
    transactions = load_data("SELECT * FROM my_schema_1.clients")

    st.dataframe(transactions, use_container_width=True, hide_index=True)
