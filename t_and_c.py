import streamlit as st
import pandas as pd
from st_db import conn  # SQLConnection de st_db

def load_data(query):
    result = conn.query(str(query))
    return pd.DataFrame(result)

def app():
    st.subheader("📊 Transactions and Clients")

    query = """
        SELECT 
            t.id AS transaction_id,
            t.amount,
            t.created_at,
            c.id AS client_id,
            c.client_name,
            c.city
        FROM my_schema_1.transactions t
        LEFT JOIN my_schema_1.clients c
            ON t.client_id = c.id
    """
    
    # load data
    transactions = load_data(query)
    st.write("🔢 Query")
    st.code(str(query),language="sql")
    st.dataframe(transactions, use_container_width=True, hide_index=True)
