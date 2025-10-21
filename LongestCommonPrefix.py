""""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
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
        
