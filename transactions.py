import streamlit as st
import pandas as pd
from st_db import conn  # SQLConnection de st_db

def load_data(query):
    result = conn.query(query)
    return pd.DataFrame(result)

def app():
    st.subheader("📊 Transactions")
    st.write("🔢 Query")
    
    query = """    
        SELECT
            id,
            client_id,
            product_id,
            transaction_date,
            amount,
            quantity,
            created_at,
            employee_id
        FROM my_schema_1.transactions
    """
    st.code(str(query),language="sql")
    
    # load data
    transactions = load_data(query)

    st.dataframe(transactions, use_container_width=True, hide_index=True)
