import streamlit as st
import streamlit.components.v1 as stc

with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()
    
stc.html(index_html)