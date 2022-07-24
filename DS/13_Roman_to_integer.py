class Solution:
    def romanToInt(self, s: str) -> int:
        
        convert_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        total = 0
        
        for i in range(len(s)-1):
            if s[i] == "I" and ( s[i+1] == "V" or s[i+1] == "X"): 
                total -= 1
            elif s[i] == "X" and ( s[i+1] == "L" or s[i+1] == "C"): 
                total -= 10
            elif s[i] == "C" and ( s[i+1] == "D" or s[i+1] == "M"): 
                total -= 100
                
            else:
                total += convert_dict[f"{s[i]}"]
        
        total += convert_dict[f"{s[len(s)-1]}"]
        return total

# sol = Solution()

# sol.romanToInt("V")