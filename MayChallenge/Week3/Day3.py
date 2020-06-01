"""
Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        d1 = collections.Counter(p)
        window = s[:len(p)-1]
        d2 = collections.Counter(window)
        for start in range(len(s)-len(p)+1):
            end = start + len(p)-1            
            d2[s[end]] = d2.get(s[end], 0) + 1
            if d1 == d2:
                res.append(start)
            # delete the start char
            d2[s[start]] -= 1
            if d2[s[start]]==0:
                del d2[s[start]]
                
        return res
            
