#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""

def canUnlockAll(boxes):
    """
    Check if all boxes can be unlocked
    """
    opened_boxes = set()
    opened_boxes.add(0)  # Start with the first box
    stack = [0]  # Initialize the stack with the first box
    
    while stack:
        current_box = stack.pop()  # Get the last box from the stack
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)  # Mark this box as opened
                stack.append(key)  # Add this box to the stack to explore later
                
    # If the size of opened_boxes is equal to the number of boxes, return True
    return len(opened_boxes) == len(boxes)
