class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        count = 0 
        zeros = 0

        for i in nums:
            if i == 0:
                zeros += 1 
            else :
                zeros = 0
            count += zeros

        return count