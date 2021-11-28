#!/usr/bin/python3
"""
Generate a list of lists of integers representing the Pascal's triangle
"""


def pascal_triangle(n):
    """Returns list of lists of integers representing Pascal's triangle of n"""
    if n <= 0:
        return []
    output = [[1]]
    for x in range(n-1):
        temp = [0] + output[-1] + [0]
        row = []
        for j in range(len(output[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
            output.append(row)

    return (output)
