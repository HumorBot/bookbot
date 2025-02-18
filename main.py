def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    num_words = get_num_words(text)
    characters = count_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    character_report(characters)
    print("--- End of report ---")
    
# Get the numnber of words in a text    
def get_num_words(text):
    words = text.split()
    return len(words)

# Get the path of the text file
def get_book_path(path):
    with open(path) as f:
        return f.read()

# Count the number of times a character appears in a text
def count_characters(text):
    char_counts = {}
    lower = text.lower()
    for char in lower:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

# Create a character report sorted by the number of times a character appears
def character_report(characters):
    sorted_dict = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_dict:
        if i.isalpha():
            print(f"The '{i}' character was found {sorted_dict[i]} times")
        


main()