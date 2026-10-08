class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        help = set(nums)
        solution = {}
        for element in help:
            solution[element] = nums.count(element)
        top_k = heapq.nlargest(k,solution.items(), lambda item : item[1])
        top_k_keys = [item[0] for item in top_k]
        return top_k_keys
