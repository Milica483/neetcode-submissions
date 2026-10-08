class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()

        for num in nums:
            dic[num] = 0
        
        for i in range(len(nums)):
            dic[nums[i]] +=1

        dic_sort = dict(sorted(dic.items(), key = lambda item:item[1], reverse = True))

        res = []

        for i in range(k):
            res.append(list(dic_sort.keys())[i])
        
        return res
            
        


        

