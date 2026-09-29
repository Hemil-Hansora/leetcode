class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt = 0
        cand = nums[0]

        for i in nums:
            if cnt == 0:
                cand = i
            if cand == i:
                cnt += 1
            else:
                cnt -= 1

        return cand
