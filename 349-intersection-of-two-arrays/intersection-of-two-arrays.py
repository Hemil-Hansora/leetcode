class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr = []
        arr_set = set()

        arr_set.update(nums1)

        for i in nums2:
            if i in arr_set and i not in arr:
                arr.append(i)

        return arr
