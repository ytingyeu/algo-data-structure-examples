import unittest
from typing import List


class Solution():
    def merge_sort(self, nums: List[int]) -> List[int]:
        def _merge_sort_rec(list_to_sort: List[int]) -> None:
            if len(list_to_sort) <= 1:
                return

            mid = len(list_to_sort) // 2
            left_part = list_to_sort[:mid]
            right_part = list_to_sort[mid:]

            _merge_sort_rec(left_part)
            _merge_sort_rec(right_part)

            idx_left, idx_right, idx_merged = 0, 0, 0

            while idx_left < len(left_part) and idx_right < len(right_part):
                if left_part[idx_left] <= right_part[idx_right]:
                    list_to_sort[idx_merged] = left_part[idx_left]
                    idx_left += 1

                else:
                    list_to_sort[idx_merged] = right_part[idx_right]
                    idx_right += 1

                idx_merged += 1

            while idx_left < len(left_part):
                list_to_sort[idx_merged] = left_part[idx_left]
                idx_left += 1
                idx_merged += 1

            while idx_right < len(right_part):
                list_to_sort[idx_merged] = right_part[idx_right]
                idx_right += 1
                idx_merged += 1

        sorted_nums = nums[:]
        _merge_sort_rec(sorted_nums)
        return sorted_nums


class TestSolution(unittest.TestCase):
    def testCase1(self):
        sol = Solution()
        nums = [5, 2, 3, 1]
        result = sol.merge_sort(nums)
        self.assertListEqual(result, [1, 2, 3, 5])

    def testCase2(self):
        sol = Solution()
        nums = [5, 1, 1, 2, 0, 0]
        result = sol.merge_sort(nums)
        self.assertListEqual(result, [0, 0, 1, 1, 2, 5])

    def testCase3(self):
        sol = Solution()
        nums = [0]
        result = sol.merge_sort(nums)
        self.assertListEqual(result, [0])

    def testCase4(self):
        sol = Solution()
        nums = [1, 0, -1, -1]
        result = sol.merge_sort(nums)
        self.assertListEqual(result, [-1, -1, 0, 1])


unittest.main()
