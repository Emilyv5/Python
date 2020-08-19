def count(nums):
    curMax = -1
    count = 0
    for num in nums:
        if num > curMax:
            curMax = num
            count = 1
        elif num == curMax:
            count +=1
    return count
print(count([1,2,3,4,4]))


