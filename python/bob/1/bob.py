def response(hey_bob):
    h_b = hey_bob.strip()
    return ("Fine. Be that way!" if not h_b else
            "Calm down, I know what I'm doing!" if h_b.isupper() and h_b.endswith("?") else
            "Whoa, chill out!" if h_b.isupper() else
            "Sure." if h_b.endswith("?") else "Whatever.")
