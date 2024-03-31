# Array traversal

## Note

in progress

## [Linear traversal](./linear-traversal)

This is the simplest type of traversal where you visit each element of the array exactly once in order. For example, finding the maximum or minimum element in an array requires a simple linear traversal.

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```

## Two-pointer traversal

In this type of traversal, you maintain two pointers (indices) into the array and move them independently. This is often used in problems where you need to find two elements that meet a certain condition. For example, in a sorted array, you can find two numbers that add up to a target value using two pointers.

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

## Sliding window traversal

In this type of traversal, you maintain a "window" of elements in the array and slide it along the array. This is often used in problems where you need to find a subarray that meets a certain condition. For example, finding the maximum sum of a subarray of a certain size.

```python
def max_subarray_sum(arr, window_size):
    window_sum = sum(arr[:window_size])
    max_sum = window_sum
    for i in range(window_size, len(arr)):
        window_sum = window_sum - arr[i - window_size] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

## Matrix traversal

In this type of traversal, you visit each element of a 2D array (matrix). This can be done in various orders: row-by-row, column-by-column, diagonally, in a spiral order, etc.

```python
def print_matrix_in_spiral_order(matrix):
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            print(matrix[top][j])
        for i in range(top + 1, bottom + 1):
            print(matrix[i][right])
        if top != bottom:
            for j in range(right - 1, left - 1, -1):
                print(matrix[bottom][j])
        if left != right:
            for i in range(bottom - 1, top, -1):
                print(matrix[i][left])

        top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
```
