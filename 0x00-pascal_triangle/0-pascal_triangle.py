#!/usr/bin/python3

"""
Returns a list of integers
representing the Pascal Triangle of n
returns empty list if n <= 0
"""

def pascal_triangle(n):
    pascal = []
    if n <= 0:
        return pascal
    pascal = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(pascal[i - 1]) - 1):
            curr = pascal[i - 1]
            temp.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
        temp.append(1)
        pascal.append(temp)
    return pascal
