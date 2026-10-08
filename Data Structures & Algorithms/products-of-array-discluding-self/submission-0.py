class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        m = 0
        zero_index = []

        for i in range(len(nums)):
            if nums[i] != 0:
                prod = prod*nums[i]
            else:
                m +=1
                zero_index.append(i)
        
        output = []
        if m > 1:
            output = [0]*len(nums)
        if m == 1:
            output = [0]*len(nums)
            output[zero_index[0]] = prod
        if m==0:
            output = [prod]*len(nums)
            for i in range(len(nums)):
                output[i] = output[i]//nums[i]
            
                

        return output

