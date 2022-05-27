import random
import unittest
from typing import List


class Solution:
    def quick_sort(self, nums: List[int]) -> List[int]:
        def _quick_sort_rec(list_to_sort: List[int], start: int, end: int):
            if start < end:
                pivot_idx = _partition(list_to_sort, start, end)
                _quick_sort_rec(list_to_sort, start, pivot_idx - 1)
                _quick_sort_rec(list_to_sort, pivot_idx + 1, end)

        def _partition(list_to_sort: List[int], start: int, end: int):
            """
            1. Swap pivot with the end of the array.
            2. Set a pointer `swap_ptr` at the beginning of the array.
            3. Iterate over the array and swap(swap_ptr, i) if array[i] < pivot.
            4. Move `swap_ptr` one step to the right after each swap in 3.
            5. After the iterattion, swap pivot (at the end of the array now) with `swap_ptr`.
            6. Return `swap_ptr` to indicate the divided point.
            """
            pivot_idx = random.randint(start, end)
            pivot_val = list_to_sort[pivot_idx]

            list_to_sort[pivot_idx], list_to_sort[end] = list_to_sort[end], list_to_sort[pivot_idx]
            swap_ptr = start

            for i in range(start, end):
                if list_to_sort[i] < pivot_val:
                    list_to_sort[swap_ptr], list_to_sort[i] = list_to_sort[i], list_to_sort[swap_ptr]
                    swap_ptr += 1

            list_to_sort[swap_ptr], list_to_sort[end] = list_to_sort[end], list_to_sort[swap_ptr]

            return swap_ptr

        res = nums[:]
        _quick_sort_rec(res, 0, len(nums) - 1)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testCase1(self):
        nums = [5, 2, 3, 1]
        result = self.sol.quick_sort(nums)
        self.assertListEqual(result, [1, 2, 3, 5])

    def testCase2(self):
        nums = [5, 1, 1, 2, 0, 0]
        result = self.sol.quick_sort(nums)
        self.assertListEqual(result, [0, 0, 1, 1, 2, 5])

    def testCase3(self):
        nums = [0]
        result = self.sol.quick_sort(nums)
        self.assertListEqual(result, [0])

    def testCase4(self):
        nums = [1, 0, -1, -1]
        result = self.sol.quick_sort(nums)
        self.assertListEqual(result, [-1, -1, 0, 1])


unittest.main()
