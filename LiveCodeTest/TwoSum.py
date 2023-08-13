class Solution:
    def twoSum(self,nums, target):
        storedItem = {}
        for i, num in enumerate(nums):
            expectedValue = target - num
            print(expectedValue)
            if expectedValue in storedItem:
                return [storedItem[expectedValue], i]
            storedItem[num] = i
        return []

# Test cases
print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
# print(Solution().twoSum([3, 2, 4], 6))       # Output: [1, 2]
# print(Solution().twoSum([3, 3], 6))          # Output: [0, 1]
