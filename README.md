# Pascal's Triangle Generator

This project contains a Python function to generate Pascal's Triangle up to `n` rows. Pascal's Triangle is a triangular array of binomial coefficients, and each row represents the coefficients of the binomial expansion.

## Function

### `pascal_triangle(n)`

Generates Pascal's Triangle up to `n` rows.

#### Parameters

- `n` (int): The number of rows in Pascal's Triangle. Must be a positive integer. If `n` is less than or equal to `0`, an empty list is returned.

#### Returns

- A list of lists, where each inner list represents a row of Pascal's Triangle.

#### Example

```python
>>> pascal_triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

#### Author
Hiba Hassanin