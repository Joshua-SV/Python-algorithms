
# insertion sort is fast for small and medium data sets, speed O(n^2)
def insetSort(nums):
    if len(nums) < 2:
        return nums

    for i in range(1,len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1],nums[j] = nums[j],nums[j-1]
            j -= 1
            
    return nums

