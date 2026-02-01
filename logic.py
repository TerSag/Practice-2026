def process_text(text):
    if not text.strip():
        return 
    return text[::-1].upper()

def calculate_length(text):
    return len(text)