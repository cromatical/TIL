from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for start_idx, start_num in enumerate(nums):
            for next_idx, next_num in enumerate(nums[start_idx + 1:]):
                if start_num + next_num == target:
                    return [start_idx, next_idx + start_idx + 1]
        return []      


if __name__=='__main__':

    test_data = [([2,7,11,15], 9),
                ([3,2,4], 6),
                ([3,3], 6)
    ]

    for nums, target in test_data:
        print(nums, target)
        print(f'Result : {Solution().twoSum(nums, target)}')
        print()