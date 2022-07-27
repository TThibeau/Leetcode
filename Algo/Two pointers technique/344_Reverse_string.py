class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        f,b = 0,len(s)-1

        while f<b:
            temp = s[b]
            s[b] = s[f]
            s[f] = temp
            f += 1
            b -= 1

        print(s)

sol = Solution()
sol.reverseString(s = ["h","e","l","l","o"])
sol.reverseString(s = ["H","a","n","n","a","h"])