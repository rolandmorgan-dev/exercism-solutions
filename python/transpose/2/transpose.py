def transpose(s : str) -> str:
    lines = s.split("\n")
    max_len = max(len(line) for line in lines)
    padded_lines = (line.ljust(max_len, '¤') for line in lines)
    result = zip(*padded_lines)
    return "\n".join("".join(line).rstrip("¤").replace("¤", " ") for line in result)