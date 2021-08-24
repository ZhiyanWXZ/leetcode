from typing import List


def generate(numRows: int) -> List[List[int]]:

    triangle = []
    for num_row in range(numRows):

        row = [None for _ in range(num_row+1)]
        row[0] = 1
        row[-1] = 1

        for j in range(1, len(row)-1):
            row[j] = triangle[num_row-1][j-1] + triangle[num_row-1][j]

        triangle.append(row)

    return triangle


if __name__ == "__main__":

    print(generate(0))