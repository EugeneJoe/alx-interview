#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def join(locked, my_keys):
    """
    Add obtained keys to our keys list
    """
    res = []
    for key in my_keys:
        res += locked[key]
    return res


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.

    Solution to the lockboxes problem
    """
    if (type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    index = 0
    keys = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for key in join(boxes, keys[index:]):
            if key not in keys:
                keys.append(key)
                index += 1
                added = True

    return len(keys) == len(boxes)
