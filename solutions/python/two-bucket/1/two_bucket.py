from collections import deque
from math import gcd

def measure(b1_max, b2_max, goal, goal_bucket):
    if goal > max(b1_max, b2_max) or goal % gcd(b1_max, b2_max) != 0:
        raise ValueError("The goal cannot be reached using the provided buckets.")

    visited = set()
    queue = deque()
    init = (b1_max, 0) if goal_bucket == "one" else (0, b2_max)
    invalid = (0, b2_max) if goal_bucket == "one" else (b1_max, 0)
    queue.append((init, 1))

    ACTIONS = (lambda b1, b2: (b1_max, b2),
               lambda b1, b2: (b1, b2_max),
               lambda b1, b2: (0, b2),
               lambda b1, b2: (b1, 0),
               lambda b1, b2: (b1 - min(b1, b2_max - b2), b2 + min(b1, b2_max - b2)),
               lambda b1, b2: (b1 + min(b2, b1_max - b1), b2 - min(b2, b1_max - b1)))

    while queue:
        (b1, b2), steps = queue.popleft()

        if (b1, b2) in visited or (b1, b2) == invalid: continue
        if b1 == goal: return steps, "one", b2
        if b2 == goal: return steps, "two", b1

        visited.add((b1, b2))
        queue.extend((action(b1, b2), steps + 1) for action in ACTIONS)

    raise ValueError("No Solution Possible.")