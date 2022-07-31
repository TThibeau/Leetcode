class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if all chars in set(s) count == t count of that char
        # Check if all chars in set(t) count == s count of that char
        # if both true -> return true, else false

        check1,check2 = [],[]
        [check1.append(s.count(c)==t.count(c)) for c in set(s)]
        [check2.append(s.count(b)==t.count(b)) for b in set(t)]
        if all(check1) and all(check2):
            return True
        else: 
            return False