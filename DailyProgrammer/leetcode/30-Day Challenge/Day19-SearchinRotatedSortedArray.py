# -*- coding: utf-8 -*-
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to 
you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        try:
            
            return nums.index(target)
        
        except:
            
            return -1