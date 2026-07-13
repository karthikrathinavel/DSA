def twoSum(nums, target):
        n = len(nums)
        if n <= 1:
            return nums
        for i in range(n):
            for j in range(i, n-1):
                if nums[j] + nums[j+1] == target:
                    return [j, j+1]
                
arr = [2,7,11,15]
target = 9
print(twoSum(arr, target))