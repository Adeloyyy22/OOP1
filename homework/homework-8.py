list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Solution:
    def plusOne(digist: list) -> list:
        list[-1] = list[-1] + 1
        print(list)

Solution.plusOne(list)
