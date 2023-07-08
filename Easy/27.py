# Easy: 27
def removeElement(nums: list[int], val: int) -> int:
    """
        Constrant: 0 <= nums[i] <= 50
        Change all non-val numbers to -1
        Reverse sort the array

        Solution 2: if num[i] != val, add num[i] to new array and increment k.
        assign new array to nums and return k    

    """
    k:int = 0
    for i in range(0, len(nums)):
        if nums[i] == val:
            nums[i] = -1
        else:
            k += 1
    
    nums.sort(reverse=True)  
    return k
