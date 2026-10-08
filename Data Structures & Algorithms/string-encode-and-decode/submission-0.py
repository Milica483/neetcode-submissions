class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for i in strs:
            s = s + str(len(i)) + "#" + i 
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        a = ""
        while(i<len(s)):
            if(s[i]!='#'):
                a += s[i]
                i+=1
            else:
                a = int(a)
                res.append(s[i+1:i+a+1])
                i = i + a + 1
                a = ""
        return res


