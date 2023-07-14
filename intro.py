import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon="👋", layout="wide"
)

st.write("# Welcome to our introduction app! 👋")

file_path = './introduction.pdf'
with open(file_path,"rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

# pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf"></iframe>'
pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf">'
    
st.markdown(pdf_display, unsafe_allow_html=True)