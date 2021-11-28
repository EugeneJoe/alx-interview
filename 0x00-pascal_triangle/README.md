# Pascal's Triangle

Pascal's Triangle is an interesting number pattern named after famous French mathematician Blaise Pascal.
To build the triangle, start with '1'at the top, then continue placing numbers below it in a triangular pattern.
Each number is the numbers directly above it added together.

```
       1
      1 1
    1  2  1
  1  3  3  1
1  4  6  4  1
```
The function defined in the file in this directory returns a nested list of integers where each list is a row in Pascal's triangle.
The triangle can be printed using the function below:

```
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
```
