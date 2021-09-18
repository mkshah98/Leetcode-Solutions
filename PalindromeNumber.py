class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x%10 is 0 and x is not 0):
            return False
        
        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x //= 10
            
        return x == reversedNum or x == reversedNum // 10
