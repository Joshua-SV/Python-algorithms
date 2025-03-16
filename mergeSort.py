
# fast O(N*logN), but consumes alot of memory space
def merge_sort(nums):
    if len(nums) < 2:
        return nums

    high = len(nums)
    mid = high // 2

    lst1 = merge_sort(nums[:mid])
    lst2 = merge_sort(nums[mid:])

    return merge(lst1, lst2)


def merge(first, second):
    lst_sorted = []

    left = 0
    right = 0

    while left < len(first) and right < len(second):
        if first[left] <= second[right]:
            lst_sorted.append(first[left])
            left += 1
        else:
            lst_sorted.append(second[right])
            right += 1

    for i in range(left, len(first)):
        lst_sorted.append(first[i])
        
    for i in range(right, len(second)):
        lst_sorted.append(second[i])
    return lst_sorted