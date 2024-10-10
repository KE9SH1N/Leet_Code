class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m = s.split()
        return(len(m[-1]))

result = Solution().lengthOfLastWord("Hello World")
print(result)