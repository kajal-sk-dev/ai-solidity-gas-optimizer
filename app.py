import streamlit as st
from src.analyzer import analyze_gas
from src.optimizer import suggest_optimization

st.set_page_config(page_title="AI Solidity Gas Optimizer")
st.title("AI Solidity Gas Optimizer")
code = st.text_area("Paste Solidity Contract:", height=300)
if st.button("Analyze Gas"):
    if code:
        st.json(analyze_gas(code))
        st.code(suggest_optimization(code), language="solidity")
    else:
        st.warning("Paste contract first")
