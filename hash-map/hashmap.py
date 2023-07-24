import string

def repeated_word(input_string):
    # Remove punctuation and convert the input string to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = input_string.translate(translator).lower()
    # Split the cleaned string into words
    words = cleaned_string.split()
    print (words)

    # Create a set to store encountered words
    encountered_words = set()

    # Iterate through the words and check if they are in the encountered_words set
    for word in words:
        if word in encountered_words:
            return word
        else:
            encountered_words.add(word)

    # If no repeated word is found, return an empty string
    return ""

# Test cases

print(repeated_word("saKHer, :   ;ahmed ahmed;; shteyat"))