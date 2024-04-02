'''
205. Isomorphic Strings
Solved
Easy
Topics
Companies

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapS2T = {}
        mapT2S = {}

        for charS, charT in zip(s, t):
            # If the character in s already has a mapping, check if it maps to the correct character in t
            if charS in mapS2T:
                if mapS2T[charS] != charT:
                    return False
            else:
                # If the character in t is already mapped to a different character in s, return false
                if charT in mapT2S:
                    return False

            # Map the characters in s to t and vice versa
            mapS2T[charS] = charT
            mapT2S[charT] = charS

        return True
