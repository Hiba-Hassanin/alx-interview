def pascal_triangle(n):
    # Handle edge case where n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the list to store rows of Pascal's Triangle
    triangle = []

    # Iterate through each row
    for i in range(n):
        # Create a row with all elements initialized to 1
        row = [1] * (i + 1)

        # Update the elements of the row, except the edges
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the completed row to the triangle
        triangle.append(row)

    # Return the completed Pascal's Triangle
    return triangle
