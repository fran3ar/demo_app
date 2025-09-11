import streamlit as st

# --- CONFIGURAR PÁGINA ---python
st.set_page_config(layout="wide")

st.sidebar.title("📌 Navigate")

page = st.sidebar.radio("Select a page:", ["Home", "Transactions","Clients","Txn & Clt","Sales By Client"])

if page == "Transactions":
    import transactions
    transactions.app()

if page == "Clients":
    import clients
    clients.app()

if page == "Txn & Clt":
    import t_and_c
    t_and_c.app()
    
if page == "Sales By Client":
    import sales_by_client
    sales_by_client.app()


elif page == "Home":
    st.subheader("Home 📂")
