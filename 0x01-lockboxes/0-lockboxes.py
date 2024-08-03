#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.

    Args:
        boxes (list of list of int): A list where each element is a list of keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''
    # Number of boxes
    n = len(boxes)

    # Initialize sets to keep track of seen and unseen boxes
    seen_boxes = set([0])  # Start with the first box unlocked
    unseen_boxes = set(boxes[0]).difference(set([0]))  # Initial unseen boxes are the ones that can be unlocked from the first box

    # Process all boxes that can be accessed
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()  # Get an unseen box to process

        # Skip invalid box indices
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue

        # If the box hasn't been seen before, process it
        if boxIdx not in seen_boxes:
            # Add all the keys from this box to the unseen_boxes set
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            # Mark this box as seen
            seen_boxes.add(boxIdx)

    # Check if all boxes are seen
    return n == len(seen_boxes)
