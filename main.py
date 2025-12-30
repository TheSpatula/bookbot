from stats import get_num_words, get_chars_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    frankenstein_txt = "./books/frankenstein.txt"
    num_words = get_num_words(get_book_text(frankenstein_txt))
    characters_found = get_chars_dict(get_book_text(frankenstein_txt))
    print(f"Found {num_words} total words")
    print(characters_found)

main()