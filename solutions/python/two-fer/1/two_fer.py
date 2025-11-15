# Determining what you will say as you give away the extra cookie.
def two_fer(name: str | None = None) -> str:
    return f"One for {name}, one for me." if name else "One for you, one for me."
