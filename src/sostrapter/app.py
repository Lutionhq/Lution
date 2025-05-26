import streamlit as st 

# app.
def success():
    """Display a success message."""
    st.success('This is a success message!', icon="✅")
    
st.button('Show Success Message', on_click=success)