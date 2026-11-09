class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        zero_run_length = 0
        total = 0

        def count_subarray(n:int):
            return n * (n + 1) // 2

        for i in nums:
            if i == 0:
                zero_run_length += 1
            else :
                total += count_subarray(zero_run_length)
                zero_run_length = 0
            
        total += count_subarray(zero_run_length)
        return total 