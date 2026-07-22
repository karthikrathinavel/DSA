class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_a = str(x)[::-1]
        print(str_a)
        if int(str_a) == x:
            return True
        else:
            return False
        

print(Solution().isPalindrome(121))