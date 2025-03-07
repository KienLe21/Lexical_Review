from transformers import pipeline

corrector = pipeline(
              'text2text-generation',
              'pszemraj/flan-t5-large-grammar-synthesis',
              )

def correct_text(text):
    prompt = f"Fix grammar and spelling: {text}"
    output = corrector(prompt, do_sample=False)
    corrected_text = output[0]["generated_text"]
    return corrected_text.replace("Fix grammar and spelling: ", "").strip()



 