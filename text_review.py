from difflib import SequenceMatcher
from nltk.translate.bleu_score import sentence_bleu
import editdistance

def evaluate_text_quality(original_text, corrected_text):
    original_words = original_text.split()
    corrected_words = corrected_text.split()

    changes = sum(1 for orig, corr in zip(original_words, corrected_words) if orig != corr)
    change_ratio = changes / len(original_words) if original_words else 0

    bleu = sentence_bleu([original_words], corrected_words)
    lev_distance = editdistance.eval(original_text, corrected_text)
    similarity = SequenceMatcher(None, original_text, corrected_text).ratio()

    return {
        "num_changes": changes,
        "change_ratio": round(change_ratio, 4),
        "bleu_score": round(bleu, 4),
        "levenshtein_distance": lev_distance,
        "similarity_score": round(similarity, 4)
    }