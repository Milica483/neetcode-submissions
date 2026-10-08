class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            help = target - num
            if help in nums:
                if nums.index(num) != nums.index(help):
                    return [nums.index(num), nums.index(help)]
                else:
                    if nums.count(num) > 1:
                        return [nums.index(num), nums.index(num,nums.index(num)+1)]