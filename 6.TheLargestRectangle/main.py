def get_largest_rectangle(histogram: list[int]):
    stack = []
    max_rectangle = 0
    for i, height in enumerate(histogram + [0]):
        while stack and histogram[stack[-1]] > height:
            top_index = stack.pop()
            rectangle = histogram[top_index] * (i - stack[-1] - 1 if stack else i)
            max_rectangle = max(max_rectangle, rectangle)
        stack.append(i)
    return max_rectangle

if __name__ == '__main__':
    assert get_largest_rectangle([2, 1, 4, 5, 1, 3, 3]) == 8
    assert get_largest_rectangle([5]) == 5
    assert get_largest_rectangle([5, 3]) == 6
    assert get_largest_rectangle([1, 1, 4, 1]) == 4
    assert get_largest_rectangle([1, 1, 3, 1]) == 4
    assert get_largest_rectangle([2, 1, 4, 5, 1, 3, 3]) == 8