# Linear traversal

## Problem statement

You are given an array of integers. Write a function `find_first_max_index` that takes this array as an argument and returns the index of the first occurrence of the maximum value in the array. If the maximum value occurs more than once, the function should return the index of the first occurrence.

### Input

The function takes an array of integers as input. You can assume that the array is non-empty and contains at least one integer.

### Output

The function should return an integer representing the index of the first occurrence of the maximum value in the array.

### Example

```python
assert find_first_max_index([1, 3, 2, 3, 1]) == 1
assert find_first_max_index([4, 4, 4, 4, 4]) == 0
assert find_first_max_index([1, 2, 3, 4, 5]) == 4
```

In the first example, the maximum value is 3 and it first occurs at index 1. In the second example, the maximum value is 4 and it first occurs at index 0. In the third example, the maximum value is 5 and it first occurs at index 4.

## Improvement

Your current solution is already quite good, but there are a few potential improvements you could make:

1. **Combine max and index operations**: Right now, you're traversing the array twice: once to find the maximum value, and once to find its index. You could do this in one pass by keeping track of the maximum value and its index as you go.
2. **Use meaningful variable names**: _max_num could be renamed to max_value for clarity.
3. **Add type hints to your tests**: This isn't necessary for the code to run, but it can make your code easier to understand and work with, especially in larger codebases.

```python
def find_first_max_index(arr: List[int]) -> int:
    if not arr:
        return -1

    max_value = arr[0]
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    return max_index
```

## Edge cases

1. **Large Inputs**: The solution has a time complexity of O(n), where n is the length of the array. This should be efficient for most inputs, but if the array is extremely large, it could still take a long time to run.
2. **Non-integer Inputs**: The function assumes that the array will only contain integers. If it's called with an array that contains non-integer values, it may not behave as expected.
3. **Memory Usage**: The solution does not use any additional memory proportional to the size of the input array, which is good. However, if the input array is extremely large, just storing the array in memory could be a problem.
