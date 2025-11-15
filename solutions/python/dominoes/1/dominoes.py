from collections import deque

def can_chain(dominoes):
    if not dominoes:
        return []
    if len(dominoes) == 1:
        return dominoes if dominoes[0][0] == dominoes[0][1] else None

    stack = deque()
    for i, d in enumerate(dominoes):
        stack.append(([(i, False)], {i}))
        if d[0] != d[1]:
            stack.append(([(i, True)], {i}))

    while stack:
        chain, used = stack.popleft()
        last_i, last_f = chain[-1]
        last_dom = dominoes[last_i]
        last_right = last_dom[1] if not last_f else last_dom[0]

        if len(chain) == len(dominoes):
            first_i, first_f = chain[0]
            first_dom = dominoes[first_i]
            first_left = first_dom[0] if not first_f else first_dom[1]
            if last_right == first_left:
                return [dominoes[i] if not f else (dominoes[i][1], dominoes[i][0]) for i, f in chain]

        for i, d in enumerate(dominoes):
            if i not in used:
                for f in (False, True):
                    left = d[0] if not f else d[1]
                    if left == last_right:
                        stack.append((chain + [(i, f)], used | {i}))
    return None
