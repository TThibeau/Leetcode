class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for i in range(len(s)):
            if not s[i] in seen.keys():
                seen[f"{s[i]}"] = 1
            else:
                seen[f"{s[i]}"] += 1

        for i in range(len(s)):
            if seen[f"{s[i]}"] == 1: 
                return i
        return -1