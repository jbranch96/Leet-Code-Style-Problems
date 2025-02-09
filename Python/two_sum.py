"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from test_runner import run_tests

# Copy entire leet code class Solution below
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        output_list: list[int]= []

        if len(nums) < 2: return []
        
        for i, num in enumerate(nums):
            target_element: int = target - num
            idx_offset: int = i+1

            if target_element in nums[idx_offset:]:
                output_list.append(i)
                output_list.append(nums[idx_offset:].index(target_element)+(idx_offset))
                return output_list

# Insert desired test cases below
"""
Example:
test_cases = [
    {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
    {"input": ([3, 2, 4], 6), "expected": [1, 2]},
    {"input": ([3, 3], 6), "expected": [0, 1]},
]
"""
test_cases = [
    {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
    {"input": ([3, 2, 4], 6), "expected": [1, 2]},
    {"input": ([3, 3], 6), "expected": [0, 1]},
]

# Replace function name with the name of the function to test: i.e., twoSum, isPalidrome, ..., etc.
"""
Example: 
run_tests(Solution, "twoSum", test_cases)
"""
if __name__ == "__main__":
    run_tests(Solution, "twoSum", test_cases)