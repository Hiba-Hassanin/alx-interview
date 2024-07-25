#!/usr/bin/python3

"""
Returns a list of integers
representing the Pascal Triangle of n
returns empty list if n <= 0
"""

def pascal_triangle(n):
    new_pascal = []
    if n <= 0:
        return new_pascal

    for i in range(n):
        row_index = [1]
        if new_pascal:
            final_row = new_pascal[-1]
            row_index.extend([sum(pair) for pair in
                              zip(final_row, final_row[1:])])
            row_index.append(1)
        new_pascal.append(row_index)
        return (new_pascal)
