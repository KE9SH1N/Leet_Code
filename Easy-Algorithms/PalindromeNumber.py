class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        
        digit = [int(digit) for digit in str(x)]
        digit.reverse()
        reversed_number = int(''.join(map(str, digit)))

        return reversed_number == x


print(Solution().isPalindrome(121))