class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]*len(nums)
        sufix = [1]*len(nums)


        for i in range(len(nums)):
            if i >0:
                prefix[i] = prefix[i-1]*nums[i -1]

                sufix[len(nums) - 1 - i] = sufix[len(nums) - i]*nums[len(nums) - i]
            
        res = []

        for i in range(len(nums)):
            res.append(sufix[i]*prefix[i])

        return res
            