#src/lution/pages/lutionsettings.py
import streamlit as st
from modules.utils.lang import LANG , LANG_CODES, LANG_NAMES
from modules.utils.sidebar import InitSidebar

InitSidebar()


if "language" not in st.session_state:
    st.session_state.language = LANG_CODES[0]

lang_choice = st.selectbox(
    "Language",
    LANG_CODES,
    format_func=lambda code: LANG_NAMES.get(code, code),
    index=LANG_CODES.index(st.session_state.language)
)
def ApplyLanguage():
    st.session_state.language = lang_choice

st.button(
    "Apply Language",
    on_click=ApplyLanguage,
    key="apply_language_button"
)
st.caption("The languages feature still in beta, we are still working on it, if you want to help us translate, please go to the [GitHub repository](https://github.com/triisdang/Lution/)")
st.caption("The language feature is not working right now.")
st.session_state.language = lang_choice
st.markdown("""Should we add something? **Feature in the [isuess](https://github.com/triisdang/Lution/issues) page!**""")

