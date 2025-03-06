import streamlit as st
from spell_checking import correct_text

st.title("Lexical Review")

# Nhập văn bản từ người dùng
input_text = st.text_area("Enter text:", "")

if st.button("Check Spelling"):
    corrected_text = correct_text(input_text)

    st.write("### **Corrected Text:**")
    st.write(corrected_text)

