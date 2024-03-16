import streamlit as st
import requests
import clipboard

def shorten_url(url):
    try:
        response = requests.get(f"http://tinyurl.com/api-create.php?url={url}", timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return "Error: Unable to shorten URL"
    except requests.exceptions.Timeout:
        return "Error: Request timed out"

def copying(shortened_url):
    clipboard.copy(shortened_url)

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>URL SHORTENER</h1>", unsafe_allow_html=True)
st.markdown("---")

form = st.form("name")
url = form.text_input("URL HERE")
s_btn = form.form_submit_button("SHORT")
if s_btn:
    shorted_url = shorten_url(url)
    st.markdown("<h3>Shortened Url</h3>", unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: center;'>{shorted_url}</h6>", unsafe_allow_html=True)
    st.button("Copy", on_click=lambda: copying(shorted_url))

