import streamlit as st

if "ERNIE_CLIENT_ID" not in st.session_state:
    st.session_state["ERNIE_CLIENT_ID"] = ""

if "ERNIE_CLIENT_SECRET" not in st.session_state:
    st.session_state["ERNIE_CLIENT_SECRET"] = ""

st.set_page_config(page_title="文心一言 Settings", layout="wide")

st.title("文心一言 Settings")

client_id = st.text_input("Client ID", value=st.session_state["ERNIE_CLIENT_ID"], max_chars=None, key=None, type='default')
client_secret = st.text_input("Client Secret", value=st.session_state["ERNIE_CLIENT_SECRET"], max_chars=None, key=None, type='default')

saved = st.button("Save")

if saved:
    st.session_state["ERNIE_CLIENT_ID"] = client_id
    st.session_state["ERNIE_CLIENT_SECRET"] = client_secret
