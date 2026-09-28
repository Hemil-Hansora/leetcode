class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = i + (j - i) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return i