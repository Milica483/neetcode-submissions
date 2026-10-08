class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = defaultdict(list)
        for str in strs:
            cnt = [0]*26
            for s in str:
                cnt[ord(s) - ord('a')] += 1
            cnt = tuple(cnt)
            solution[cnt].append(str)
        return(list(solution.values()))
        
    
        


        