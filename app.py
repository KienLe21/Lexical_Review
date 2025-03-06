import streamlit as st
from spell_checking import correct_text
from text_review import evaluate_text_quality

st.title("Lexical Review")

# Nhập văn bản từ người dùng
input_text = st.text_area("Enter text:", "")

if st.button("Check Spelling & Grammar"):
    if input_text.strip():
        corrected_text = correct_text(input_text)
        metrics = evaluate_text_quality(input_text, corrected_text)

        st.write("### **Corrected Text:**")
        st.write(corrected_text)

        # Hiển thị kết quả đánh giá
        st.write("### **Evaluation Metrics:**")
        st.write(f"🔹 **Number of Changes:** {metrics['num_changes']}")
        st.write(f"🔹 **Change Ratio:** {metrics['change_ratio']:.4f}")
        st.write(f"🔹 **BLEU Score:** {metrics['bleu_score']:.4f}")
        st.write(f"🔹 **Levenshtein Distance:** {metrics['levenshtein_distance']}")
        st.write(f"🔹 **Similarity Score:** {metrics['similarity_score']:.4f}")
    else:
        st.warning("Please enter some text.")



