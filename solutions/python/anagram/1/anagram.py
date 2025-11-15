# Function for finding anagram words
def find_anagrams(word: str, candidates: list) -> list:
    results = []
    s_word = sorted(word.lower())
    for candidate in candidates:
        s_candidate = sorted(candidate.lower())
        if candidate.lower() != word.lower() and s_candidate == s_word:
            results.append(candidate)
    return results