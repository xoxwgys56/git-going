from typing import List


def find_first_max_index(arr: List[int]) -> int:
    # Your code goes here
    if not arr:
        return -1

    _max_num = max(arr)

    return arr.index(_max_num)


def test_find_first_max_index():
    assert find_first_max_index([1, 3, 2, 3, 1]) == 1
    assert find_first_max_index([4, 4, 4, 4, 4]) == 0
    assert find_first_max_index([1, 2, 3, 4, 5]) == 4
    assert find_first_max_index([5, 4, 3, 2, 1]) == 0  # Test with decreasing array
    assert (
        find_first_max_index([1]) == 0
    )  # assert find_first_max_index([]) == -1 Test with single element array
    assert (
        find_first_max_index([1, 1, 1, 1, 2, 2, 2, 2]) == 4
    )  # Test with repeated max value
    assert find_first_max_index([-1, -2, -3, -4, -5]) == 0  # Test with negative numbers
    assert find_first_max_index([]) == -1
    print("All tests passed.")


if __name__ == "__main__":
    test_find_first_max_index()
