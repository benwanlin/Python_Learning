from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            print(i)
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                return [i, nums.index(diff)]

s = Solution()
print(s.twoSum([3,2,4], 6))