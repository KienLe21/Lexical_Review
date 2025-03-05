import streamlit as st
from spell_checking import correct_text

st.title("Lexical Review")

# Nhập văn bản từ người dùng
input_text = st.text_area("Enter text:", "")

if st.button("Check Spelling"):
    corrected_text = correct_text(input_text)

    st.write("### **Corrected Text:**")
    st.write(corrected_text)

    # Lưu kết quả vào file
    with open("spellchecked_output.txt", "w") as f:
        f.write(corrected_text)
    
    st.success("Corrected text saved to `spellchecked_output.txt`!")
