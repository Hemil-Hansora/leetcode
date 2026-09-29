class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        max_freq = 0
        max_num = None

        for num in freq:
            if freq[num] > max_freq:
                max_freq = freq[num]
                max_num = num

        return max_num
