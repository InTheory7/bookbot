def word_count(book_str):
    # Split the string into words based on whitespace:
    words = book_str.split()
    # Return the number of words:
    return len(words)

def char_counts(book_str):
    # Convert the string to all lowercase:
    book_str = book_str.lower()
    # Keep a tally of each character. When a new
        # character appears, add it to the dictionary,
        # otherwise, increment the count:
    char_dict = {}
    for char in book_str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def generate_report(book_path, word_tot, char_tots):
    # Print introduction:
    print(f"--- Book information for {book_path}")
    # Print word total:
    print(f"{word_tot} words found in the document")

    # Sort character dictionary by frequency (only
        # possible in Python 3.7 or later):
    sorted_char_tots = sorted(char_tots, key=char_tots.get, reverse=True)
    # ^ This step is done differently in the hint

    # Loop through and print the key:value pairs:
    for key in sorted_char_tots:
        # Only print the letters and their frequencies:
        if key.isalpha():
            print(f"{key} appears {char_tots[key]} times")
    
    # Print ending:
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    # Read the book file:
    with open(book_path) as f:
        file_contents = f.read()
    # Get the number of words and print:
    word_tot = word_count(file_contents)

    # Get the number of appearences of each character:
    char_tots = char_counts(file_contents)

    # Generate a report of this information:
    generate_report(book_path, word_tot, char_tots)

main()