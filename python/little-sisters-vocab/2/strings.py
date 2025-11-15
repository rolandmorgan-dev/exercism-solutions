"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    # Adding "un" before a word
    return "un" + word

def make_word_groups(vocab_words):
    # Adding the prefix before the words
    prefix = vocab_words.pop(0)
    full_string = ""
    for index, word in enumerate(vocab_words):
        full_string += " :: " + prefix + word
    return prefix + full_string
    
def remove_suffix_ness(word):
    # if iness at the end of the word, then replace with y
    # otherwise if ness only, then remove it from the word
    return word.replace("iness","y",1) if "iness" in word else word.replace("ness","",1)

def adjective_to_verb(sentence, index):
    # extracting indexed word, removing "." if needed.
    return sentence.split()[index].replace(".","")+"en" if "." in sentence.split()[index] else sentence.split()[index]+"en"