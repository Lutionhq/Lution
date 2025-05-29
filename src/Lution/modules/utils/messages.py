import streamlit as st


def success(message: str = "Operation completed successfully."):
    """Display a success message."""
    st.success(message, icon="✅")
def warning(message: str = "Holy! the dev forgot to write this warning messsage lol 💀."):
    """Display a warning message."""
    st.warning(message, icon="⚠️")

def skull(message: str = "💀"):
    """Display a skull message."""
    st.info(message, icon="💀")