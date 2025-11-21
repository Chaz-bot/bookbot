def count_words(book):
    file = open(book, "r")
    content = file.read()
    file.close()
    
    words = content.split()
    
    num_words = 0
    for word in words:
        num_words += 1

    return num_words

def count_characters(book):
    file = open(book, "r")
    content = file.read()
    file.close()
    
    content = content.lower()
    char_dict = {}

    for ch in content:
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1

    return char_dict    

def sort_list(char_dict):
    sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars