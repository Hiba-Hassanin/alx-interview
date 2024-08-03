#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)

    # Track which boxes are unlocked
    unlocked = [False] * n
    unlocked[0] = True

    # Use a queue for BFS
    queue = deque([0])

    while queue:
        # Get the next box
        current_box = queue.popleft()

        # Check all keys in the current box
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                # Mark the box as unlocked and add to queue
                unlocked[key] = True
                queue.append(key)

    # Return True if all boxes are unlocked, otherwise False
    return all(unlocked)
