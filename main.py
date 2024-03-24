def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_book_stats(book_path,sort_on(count_letters(text)))

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return text.split()

def count_letters(text):
    # strip whitespaces
    stripped_string = text.strip()
    stripped_string = stripped_string.replace(" ", "")
    # convert to lowercase
    lowered_string = stripped_string.lower()
    # remove punctuation
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    no_punctuation_string = lowered_string
    for char in punctuation:
        no_punctuation_string = no_punctuation_string.replace(char, '')
    
    letter_counts = {}
    for char in no_punctuation_string:
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts

def sort_on(dict):
    #sort dict highest to lowest
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)

def print_book_stats(book_path, stats):
    print(f"--- Begin report of {book_path} ---")
    #words found in book
    print(f"{str(len(count_words(get_book_text(book_path))))} words found in the document\n")
    for stat in stats:
        print("The character '" + stat[0] + "' was found "  + str(stat[1]) + " times")

    print("--- End report ---")

main()