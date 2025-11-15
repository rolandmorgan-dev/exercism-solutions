vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def translate(text):
    words = []

    for word in text.split():

        # consonant before "qu"
        cons_before_qu = 0
        if "qu" in word:
            index_qu = word.index("qu")
            if index_qu-1 >= 0 and word[index_qu-1] in consonants:
                cons_before_qu = 1

        # Rule 1
        # if word starts with vowel or "xr", "yt" then add "ay" to end
        if word[0] in vowels or word.startswith(("xr","yt")):
            words.append(word+"ay")

        # Rule 3
        # if "qu" in word, index_qu above 0, given index is a consonant
        elif word.startswith("qu") or cons_before_qu:
            cons_before_qu = ""
            build_word = word
            # if chars before qu, find consonant ones
            for char in word[:index_qu]:
                # if any consonants before qu
                # build a string from them
                if char in consonants:
                    cons_before_qu += char
                    build_word = build_word.replace(char, "", 1)
                else: break
            build_word = build_word.replace("qu", "", 1)
            words.append(build_word + cons_before_qu + "quay")
        
        # Rule 4
        # if word starts with consonant, word has "y"
        elif word[0] in consonants and "y" in word and word[0] != "y":
            index_y = word.index("y")
            cons_before_y = ""
            build_word = word
            # if chars before y, find consonant ones
            for char in word[:index_y]:
                # if any consonants before y
                # build a string from them
                if char in consonants:
                    cons_before_y += char
                    build_word = build_word.replace(char, "", 1)
                else: break
            words.append(build_word + cons_before_y + "ay")
        
        # Rule 2
        # if a word begins with one or more consonants
        elif word[0] in consonants:
            cons_in_a_row = ""
            build_word = word
            # find consonant followed by consonant
            for char in word:
                # build a string from consonant ones
                if char in consonants:
                    cons_in_a_row += char
                    build_word = build_word.replace(char, "", 1)
                else: break
            words.append(build_word + cons_in_a_row + "ay")

    return " ".join(words)