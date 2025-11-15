import re

# Function to count words in a sentence -> s
def count_words(s : str) -> dict:
    word_count = {}
    first_phase = re.sub(r"[^\w\' 	]*", "", re.sub("[,_]+"," ", s)).split()
    for word in first_phase:
        word = word.strip("'").lower()
        if word in word_count: word_count[word] += 1
        else: word_count[word] = 1
    return word_count