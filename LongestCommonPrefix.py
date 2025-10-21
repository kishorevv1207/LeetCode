class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        key = min(strs, key=len)
        out=""
        for i in range(0,len(key)):
            check = list()
            for j in strs:
                check.append(j[i])
            check=set(check)
            if len(check)==1:
                out+=list(check)[0]
            else:
                break
        return out
        
