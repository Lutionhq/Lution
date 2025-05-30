#src/lution/pages/lutionsettings.py
import streamlit as st
from modules.utils.lang import LANG , LANG_CODES, LANG_NAMES



lang_choice = st.selectbox(
    "Language",
    LANG_CODES,
    format_func=lambda code: LANG_NAMES.get(code, code),
    index=LANG_CODES.index(st.session_state.language)
)
st.caption("The languages feature still in beta, we are still working on it, if you want to help us translate, please go to the [GitHub repository](https://github.com/triisdang/Lution/)")
st.session_state.language = lang_choice
st.markdown("""Should we add something? **Feature in the [isuess](https://github.com/triisdang/Lution/issues) page!**""")

