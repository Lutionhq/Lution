import streamlit as st 

# app.
def success():
    """Display a success message."""
    st.success('', icon="✅")
    
modstab , apprtab, about = st.tabs(["Mods", "Apppearance","About"])

with modstab:
    st.header("Mods")
    st.write("This is the Mods tab. You can add your mods here.")
    st.button("Add Mod", on_click=success)

with apprtab:
    st.header("Appearance")
    st.write("This is the Appearance tab. You can customize the appearance here.")
    st.button("Change Appearance", on_click=success)
with about:
    st.header("About")
    '''
    This project made by Chip, using Streamlit, made possible with [Sober](https://sober.vinegarhq.org/).
    
    You can find the source code on [GitHub](https://github.com/triisdang/Sostrapter)

    Thank you for using Sostrapter!❤️
    '''

