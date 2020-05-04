"""
Number Complement
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""
class Solution:
    def findComplement(self, num: int) -> int:
        x=bin(num)[2:]
        print(x)
        return num^(2**len(x)-1)
        
