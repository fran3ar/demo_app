import streamlit as st
import pandas as pd
from st_db import conn  # SQLConnection de st_db

def load_data(query):
    result = conn.query(str(query))
    return pd.DataFrame(result)

def app():
    st.subheader("📊 Sales by Client")

    query = """
        SELECT 
            c.id AS client_id,
            c.client_name,
            SUM(t.amount) AS total_amount
        FROM my_schema_1.transactions t
        LEFT JOIN my_schema_1.clients c
            ON t.client_id = c.id
        GROUP BY c.id, c.client_name
        ORDER BY total_amount DESC
    """
    
    # load data
    transactions = load_data(query)
    st.write("🔢 Query")
    st.code(str(query),language="sql")
    st.dataframe(transactions, use_container_width=True, hide_index=True)
