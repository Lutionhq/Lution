import streamlit as st
def success(message: str = "Operation completed successfully."):
    """Display a success message."""
    st.success(message, icon="✅")
