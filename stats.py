def get_num_words(text):
    words = text.split()
    
    return len(words)

def get_chars_dict(text):
    counts = {}          # start empty

    for ch in text:
        ch = ch.lower()  # normalize

        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    return counts