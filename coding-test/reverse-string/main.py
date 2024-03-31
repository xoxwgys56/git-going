def reverse_string(s):
    # TODO: Implement your solution here
    res = s[::-1]
    return res

def reverse_string_in_place(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    return s

def test_reverse_string():
    assert reverse_string(list("hello")) == list("olleh")
    assert reverse_string(list("Python")) == list("nohtyP")
    assert reverse_string(list("")) == list("")
    assert reverse_string(list("a")) == list("a")
    assert reverse_string(list("ab")) == list("ba")
    assert reverse_string(list("abc")) == list("cba")
    assert reverse_string(list("racecar")) == list("racecar")
    print("All tests passed.")

if __name__ == "__main__":
    test_reverse_string()