from string import ascii_uppercase as alpha

# Diamond shaped letters
def rows(letter : str) -> list:
    sq_lenght = alpha.index(letter) * 2 + 1
    letter_index = alpha.index(letter) + 1
    result = []

    # Creating the first half of the shape
    for i in range(letter_index):
        rows = [" "] * sq_lenght
        rows[sq_lenght // 2 - i] = alpha[i]
        rows[sq_lenght // 2 + i] = alpha[i]
        result.append("".join(rows))

        # Creating the second half of the shape
        if i == letter_index - 1:
            for inner in reversed(range(letter_index - 1)):
                rows = [" "] * sq_lenght
                rows[sq_lenght // 2 - inner] = alpha[inner]
                rows[sq_lenght // 2 + inner] = alpha[inner]
                result.append("".join(rows))

    return result
