class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        b = 0
        for num in nums_set:
            if num-1 not in nums_set:
                # start counting
                a = 1
                num_help = num + 1
                while(True):
                    if num_help in nums_set:
                        a = a +1
                        num_help = num_help + 1
                    else:
                        if b<a and a != 100001:
                            b = a
                        break
        
        return b 
                    
                    
