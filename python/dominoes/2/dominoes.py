from collections import deque

def can_chain(dominoes):
    # Handle base cases
    if not dominoes:
        return []
    if len(dominoes) == 1:
        return dominoes if dominoes[0][0] == dominoes[0][1] else None
    
    # Each stack item is a path: list of (domino, index) tuples
    stack = deque()
    for idx, domino in enumerate(dominoes):
        stack.append([(domino, idx)])
        stack.append([(domino[::-1], idx)])
    
    # Static domino variants with original indices
    domino_set = tuple(stack)
    
    while stack:
        current = stack.popleft()
        current_indices = {idx for _, idx in current}
        for [(domino, idx)] in domino_set:
            if domino[0] == current[-1][0][1] and idx not in current_indices:
                if len(current) + 1 == len(dominoes) and domino[1] == current[0][0][0]:
                    return [domino for domino, _ in current + [(domino, idx)]]
                stack.append(current + [(domino, idx)])