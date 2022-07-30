class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Solution 1
        # make hash table of magazine elements
        # for each char in ransomNote, check if available in hash table

        # mh = {}
        # for c in magazine:
        #     if not c in mh.keys():
        #         mh[c] = 1
        #     else:
        #         mh[c] += 1
        
        # for l in ransomNote:
        #     if l in mh.keys():
        #         if mh[l]==1:
        #             del mh[l]
        #         else: 
        #             mh[l] -= 1
        #     else:
        #         return False
        # return True

        # Solution 2:
        # for each char in ransomnote, check if the count of that char occurrence is <= count of that char in magazine
        # for c in ransomNote:
        #     if ransomNote.count(c) > magazine.count(c): 
        #         return False
        # return True

        # Solution 3:
        # Check count again, but make ransomnote a set (removes duplicates) to avoid checking same char more than once
        # Very fast!
        # Credits to o_sharp for this solution 3: https://leetcode.com/problems/ransom-note/discuss/85940/Many-different-ways%3A-1-liners-2-liners-and-Concise-4-liner-in-Python-80ms
        return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))