"""
Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) >len(s2) :
            return False
        
        len_s1= len(s1) 
        s1_count=Counter(s1) 
        w_count=Counter() 
        
        for i,c in enumerate(s2) :
            w_count[c]+=1
            
            if i>=len_s1:
                eleft=s2[i-len_s1]
                if w_count[eleft]==1:
                    del w_count[eleft]
                else:
                    w_count[eleft]-=1
                
            if w_count==s1_count:
                return True
        return False
