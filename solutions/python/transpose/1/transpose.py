def transpose(text):
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)

    transposed = []
    for i in range(max_len):
        list_len = max(last+1 for last, line in enumerate(lines) if i < len(line))
        build_line = [" "] * list_len
        for index, line in enumerate(lines):
            if i < len(line):
                build_line[index] = line[i]

        transposed.append("".join(build_line))

    return "\n".join(transposed)