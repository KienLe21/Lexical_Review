from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load model and tokenizer
device = torch.device("cpu")
tokenizer = AutoTokenizer.from_pretrained("Bhuvana/t5-base-spellchecker")
model = AutoModelForSeq2SeqLM.from_pretrained("Bhuvana/t5-base-spellchecker").to(device)

def correct_text(text):
    sentences = text.split('. ')
    corrected_sentences = []

    for sentence in sentences:
        if not sentence:
            continue

        # Chuyển chữ cái đầu thành viết thường
        lowercase_sentence = sentence[0].lower() + sentence[1:] if sentence else sentence

        input_ids = tokenizer.encode(lowercase_sentence, return_tensors='pt').to(device)

        sample_output = model.generate(
            input_ids,
            do_sample=True,
            max_length=50,
            top_p=0.99,
            num_return_sequences=1
        )

        corrected_sentence = tokenizer.decode(sample_output[0], skip_special_tokens=True)

        # Viết hoa chữ cái đầu sau khi sửa
        corrected_sentence = corrected_sentence[0].upper() + corrected_sentence[1:] if corrected_sentence else corrected_sentence

        corrected_sentences.append(corrected_sentence)

    return ". ".join(corrected_sentences)

