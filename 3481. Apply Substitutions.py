'''

You are given a replacements mapping and a text string that may contain placeholders formatted as %var%, where each var corresponds to a key in the replacements mapping. Each replacement value may itself contain one or more such placeholders. Each placeholder is replaced by the value associated with its corresponding replacement key.

Return the fully substituted text string which does not contain any placeholders.

 

Example 1:

Input: replacements = [["A","abc"],["B","def"]], text = "%A%_%B%"

Output: "abc_def"

Explanation:

    The mapping associates "A" with "abc" and "B" with "def".
    Replace %A% with "abc" and %B% with "def" in the text.
    The final text becomes "abc_def".

Example 2:

Input: replacements = [["A","bce"],["B","ace"],["C","abc%B%"]], text = "%A%_%B%_%C%"

Output: "bce_ace_abcace"

Explanation:

    The mapping associates "A" with "bce", "B" with "ace", and "C" with "abc%B%".
    Replace %A% with "bce" and %B% with "ace" in the text.
    Then, for %C%, substitute %B% in "abc%B%" with "ace" to obtain "abcace".
    The final text becomes "bce_ace_abcace".


'''

from typing import List

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        d = dict(replacements)
        memo = {}

        def resolve(key):
            if key in memo:
                return memo[key]
            
            
            val = d[key]
            result = ""
            i = 0
            while i < len(val):
                if val[i] == "%" and i + 1 < len(val):
                    j = i + 1
                    while j < len(val) and val[j] != "%":
                        j += 1
                    if j < len(val):  
                        nested_key = val[i+1:j]
                        result += resolve(nested_key)
                        i = j + 1
                    else:
                        result += val[i]
                        i += 1
                else:
                    result += val[i]
                    i += 1

            memo[key] = result
            return result

        result = ""
        i = 0
        while i < len(text):
            if text[i] == "%" and i + 1 < len(text):
                j = i + 1
                while j < len(text) and text[j] != "%":
                    j += 1
                if j < len(text):  
                    key = text[i+1:j]
                    result += resolve(key)
                    i = j + 1
                else:
                    result += text[i]
                    i += 1
            else:
                result += text[i]
                i += 1

        return result
