import streamlit as st
from modules.muti_instance.SoberManager import SoberManager
from modules.utils.sidebar import InitSidebar

InitSidebar()

sm = SoberManager

@st.dialog("Add A new Sober Instance")
def ask():
    st.write("With Sober instance, you can have many accounts on each instance and launch them all at once!")
    InstanceName = st.text_input(label="Instance name", placeholder="e.g: Profile1, MyNewAccount")
    if st.button("Add"):
        st.rerun()

if st.button("Add new Instance") :
    ask()
