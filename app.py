import streamlit as st

from utils.nav_pages import build_pages
from utils.session import restore_login

st.set_page_config(page_title="法律申論題眾包平台")

restore_login(st)

pages = build_pages(st.session_state.get("logged_in"))
pg = st.navigation(pages)
pg.run()
