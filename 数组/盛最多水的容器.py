from typing import List


def maxArea(height: List[int]) -> int:

    i = 0
    j = len(height) - 1
    max_area = 0
    while i < j:

        if height[i] >= height[j]:
            area = (j - i) * height[j]
            j -= 1
        else:
            area = (j - i) * height[i]
            i += 1
        if max_area < area:
            max_area = area

    return max_area


if __name__ == "__main__":
    height = [1,2]
    print(maxArea(height))