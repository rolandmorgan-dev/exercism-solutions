def egg_count(spots : int) -> int:
    return sum(int(egg) for egg in str(bin(spots)[2:]))
