import streamlit as st
from spell_checking import correct_text
import difflib

st.title("Lexical Review")

# Nhập văn bản từ người dùng
input_text = st.text_area("Enter text:", "")

def highlight_corrections(original, corrected):
    """ So sánh và tìm lỗi đã sửa giữa văn bản gốc và văn bản chỉnh sửa """
    original_words = original.split()
    corrected_words = corrected.split()
    
    diffs = list(difflib.ndiff(original_words, corrected_words))
    corrections = []

    word_wrong, word_correct = None, None

    for diff in diffs:
        if diff.startswith('- '):  # Từ bị xóa (tức là từ sai)
            word_wrong = diff[2:]
        elif diff.startswith('+ '):  # Từ được thêm vào (tức là từ đúng)
            word_correct = diff[2:]
            if word_wrong:  # Nếu có từ sai tương ứng, thì lưu lại cặp lỗi -> sửa
                corrections.append(f"🔹 **{word_wrong}** → **{word_correct}**")
                word_wrong, word_correct = None, None

    return corrections

if st.button("Check Spelling & Grammar"):
    if input_text.strip():
        corrected_text = correct_text(input_text)

        corrections = highlight_corrections(input_text, corrected_text)
        changes = len(corrections)
        change_ratio = changes / len(input_text.split()) if input_text else 0
        change_ratio_percent = f"{round(change_ratio * 100, 2)}%"

        col1, col2 = st.columns([1, 2])  # Chia layout thành hai cột, cột phải rộng hơn

        with col1:
            st.write("### **Current Errors:**")
            if corrections:
                for correction in corrections:
                    st.write(f"- {correction}")
            else:
                st.write("✅ No corrections needed!")

        with col2:
            st.write("### **Evaluation Metrics:**")
            st.write(f"🔹 **Number of Errors:** {changes}")
            st.write(f"🔹 **Error Ratio:** {change_ratio_percent}")

            st.write("### **Corrected Text:**")
            st.write(corrected_text)
    else:
        st.warning("Please enter some text.")



