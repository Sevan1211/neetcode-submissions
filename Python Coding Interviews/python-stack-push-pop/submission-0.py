from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    result = []
    for num in arr[::-1]:
        result.append(num)

    return result



# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
