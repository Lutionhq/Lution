import streamlit as st
from modules.muti_instance.SoberManager import SoberManager
from modules.utils.sidebar import InitSidebar

InitSidebar()


@st.dialog("Add A new Sober Instance")
def ask():
    st.write("With Sober instance, you can have many accounts on each instance and launch them all at once!")
    InstanceName = st.text_input(label="Instance name", placeholder="e.g: Profile1, MyNewAccount")
    if st.button("Add"):
        SoberManager.add_instance(InstanceName)
        st.success("Success! Don't spam it or its will trash your app folder....")
       
        
st.write("Run sudo chmod -R 777 /var/lib/flatpak/app/ before create an instance")
if st.button("Add new Instance") :
    ask()
