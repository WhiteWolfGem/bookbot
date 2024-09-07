def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def print_report(bookPath, wordCount, chars):
    print(f"--- Begin report of {bookPath} ---")
    print(f"{wordCount} words found in the document\n")

    sortedChars = dict(sorted(
        chars.items(),
        reverse=True,
        key=lambda x: x[1])).items()

    for key, value in sortedChars:
        if str(key).isalpha():
            print(f"The '{key}' character was found {value} times")

    print("--- End Report ---")


main()
