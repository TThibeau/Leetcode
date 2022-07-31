class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = {}       # hash table that stores the characters seen in the substring
        f,e = 0,1       # Two pointers front and end

        if len(s)==0: return 0
        if len(s)==1: return 1
        
        seen[s[f]] = 1

        while e<len(s): # once the end pointer reaches the end of the string, the search is done
            if not s[e] in seen.keys():
                seen[s[e]] = 1
                e += 1
                
                if e-f > max_length:
                    max_length = e-f
            else:
                if e-f > max_length:
                    max_length = e-f
                
                del seen[s[f]]

                f += 1
                
        return max_length