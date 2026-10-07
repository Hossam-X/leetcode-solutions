"""
LeetCode 1 - Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Hash Map

Approach: store each number's index in a dict; for every number,
check if (target - number) was already seen.

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
