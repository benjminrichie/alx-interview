#!/usr/bin/python3
"""Lockboxes Solved 100%"""


def canUnlockAll(boxes):
    """Checks if all the boxes can be opened"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for k in range(1, len(boxes) - 1):
        unlocked = False
        for i in range(len(boxes)):
            unlocked = k in boxes[i] and k != i
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True
