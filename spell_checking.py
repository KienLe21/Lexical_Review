from transformers import pipeline

corrector = pipeline(
              'text2text-generation',
              'pszemraj/flan-t5-large-grammar-synthesis',
              )

def correct_text(text):
    prompt = f"Fix grammar and spelling: {text}"
    output = corrector(prompt, do_sample=False)
    corrected_text = output[0]["generated_text"]

    # Loại bỏ prompt khỏi kết quả
    corrected_text = corrected_text.replace("Fix grammar and spelling: ", "").strip()

    # Kiểm tra chữ cái đầu và viết hoa nếu cần
    if corrected_text and corrected_text[0].islower():
        corrected_text = corrected_text[0].upper() + corrected_text[1:]

    return corrected_text




 