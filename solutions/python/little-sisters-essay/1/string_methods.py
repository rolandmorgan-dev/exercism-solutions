"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    #Capitalize first letters in the title.
    return title.title()


def check_sentence_ending(sentence):
    #Checking if the sentence ends with a dot.
    return sentence.endswith(".")


def clean_up_spacing(sentence):
    #Cleaning up spaces on both sides in the string object.
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    #Replacing a word in the provided sentence with a new one.
    return sentence.replace(old_word, new_word)
