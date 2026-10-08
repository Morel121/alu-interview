def pascal_triangle(n):
    """
    Returns a list of lists of integers representing 
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        # Build the current row using the sum of adjacent elements from the previous row
        current_row = [1]
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
