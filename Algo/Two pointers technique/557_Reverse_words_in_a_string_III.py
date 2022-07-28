class Solution:
    def reverseWords(self, s: str) -> str:
        low = s.split(" ")

        for i in range(len(low)):
            word = list(low[i])

            f,b = 0, len(word)-1

            while f<b:
                temp = word[f]
                word[f] = word[b]
                word[b] = temp
                f += 1
                b -= 1
            low[i] = "".join(word)

        s = " ".join(low)
        # print(s)
        return s


sol = Solution()
sol.reverseWords(s = "Let's take LeetCode contest")