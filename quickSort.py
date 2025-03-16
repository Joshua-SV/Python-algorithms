# widely used to sort large data better tha merge sort at O(N*logN) but no extra space used
def quick_sort(nums, low, high):
    if len(nums) < 2:
        return nums

    if low < high:
        mid = partition(nums, low, high)
        # sort left half
        quick_sort(nums, low, mid-1)
        # sort right half
        quick_sort(nums, mid+1, high)

def partition(nums, low, high):
    # set the pivot to be the last element
    pivot = nums[high]

    # i will be our swap index
    i = low - 1

    for j in range(low,high):
        # if the j index is less than pivot value
        if nums[j] < pivot:
            # swap using the i index
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    # after all elements are swapped based on pivot then swap pivot with i
    i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
