import sys
from stats import num_words, count_chars, sort_char_counts

def main():
    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from the command line argument
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Load book text
    text = get_book_text(book_path)

    # Word count
    word_count = num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Character count
    print("--------- Character Count -------")
    char_count = count_chars(text)
    sorted_chars = sort_char_counts(char_count)

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

main()
