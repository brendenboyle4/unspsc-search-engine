def normalize_text(text):
    """Normalize the input text by converting to lowercase and stripping whitespace."""
    return text.lower().strip()

def extract_keywords(text):
    """Extract keywords from the input text for better search matching."""
    return [word for word in normalize_text(text).split() if word]

def remove_special_characters(text):
    """Remove special characters from the input text."""
    import re
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def preprocess_input(text):
    """Preprocess the input text for improved search accuracy."""
    text = remove_special_characters(text)
    return extract_keywords(text)