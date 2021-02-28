import copy
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(nums: List[int], single_res: List[int], res: List[List[int]]):
            if not nums:
                res.append(single_res)
            else:
                single_res_without = copy.copy(single_res)
                single_res_with = copy.copy(single_res)
                single_res_with.append(nums[0])
                solve(nums[1:], single_res_without, res)
                solve(nums[1:], single_res_with, res)
        res = []
        solve(nums, [], res)
        return res


nums = [1, 2, 3]

sol = Solution()
print(sol.subsets(nums))
