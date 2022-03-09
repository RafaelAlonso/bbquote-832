import streamlit as st
from bbquote.get_quote import get_quote

st.markdown('# Welcome to the BBQuotes website')

st.markdown('## Check this one out:')
st.markdown(get_quote())