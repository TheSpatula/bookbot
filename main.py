def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def main():
    frankenstein_txt = "./books/frankenstein.txt"
    num_words = get_num_words(get_book_text(frankenstein_txt))
    print(f"Found {num_words} total words")

main()