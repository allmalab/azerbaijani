from .config import schwa_min_threshold, min_text_length


def is_azerbaijani(text: str):
    if len(text) < min_text_length:
        raise ValueError("Text is too short.")

    text = text.lower()
    text = text.replace(" ", "")

    schwa_ratio = sum([char == "ə" for char in text]) / len(text)

    return schwa_ratio > schwa_min_threshold
