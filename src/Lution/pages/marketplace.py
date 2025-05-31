import streamlit as st
from modules.utils.sidebar import InitSidebar

InitSidebar()
st.header("Marketplace")

# thc = st.container(border=True)

# thc.markdown("""### Themes""")

# cnthc = thc.container(border=True)

# cnthc.markdown("""###### Better Default""")
# cnthc.button("Install")


def create_container(title: str, border: bool = True):
    container = st.container(border=border)
    container.markdown(f"### {title}")
    return container

def create_columns(contents):
    cols = st.columns(len(contents), border=True)
    for idx, (col, content) in enumerate(zip(cols, contents)):
        with col:
            st.markdown(f"### {content.get('title', 'Untitled')}")
            if "body" in content:
                st.markdown(content.get("body", "No description provided."))
            if "image" in content:
                st.image(content.get("image"), use_container_width=True)
            else:
                st.image("https://placehold.co/600x400?text=No+Image", use_container_width=True)
            if "button" in content:
                st.button(content.get("button"), key=f"{content.get('title', 'Untitled')}_btn_{idx}")

contents = [
    {"title": "Better Default", "body": "A better default theme for Lution.", "button": "Install"},
    {"title": "Dark Mode", "body": "A dark mode theme for Lution.", "button": "Install"},
    {"title": "Light Mode", "body": "A light mode theme for Lution.", "button": "Install"},
]
create_columns(contents)