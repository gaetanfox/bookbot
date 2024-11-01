def main():
    book_path = "frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    get_book_report(chars_dict, num_words)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_book_report(chars_dict, num_words):
    print(num_words)
    for stuff in chars_dict.items():
        if len(stuff) >= 1:
            print(f"The '{stuff[0]}' character was found {stuff[1]} times")


main()
