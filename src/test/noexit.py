import streamlit as st

# Hide the default 'X' button
st.html(
    """
    <style>
    div[aria-label="dialog"] > button[aria-label="Close"] {
        display: none;
    }
    div.stDialog backdrop-selector { pointer-events: none; }
    </style>
    """
)

@st.dialog("Important Dialog")
def my_dialog():
    st.write("User must click Confirm")
    if st.button("Confirm"):
        st.session_state.dialog_closed = True
        st.rerun()

if st.button("Open dialog"):
    my_dialog()
