from stats import *
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    sorted_list = sort_list(count_characters(sys.argv[1]))

    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {count_words(sys.argv[1])} total words
--------- Character Count -------""")

    for ch, count in sorted_list:
        if ch.isalpha():
            print(f"{ch}: {count}")

    print("============= END ===============")

main()