class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # Store the number in a variable
        number = x
        # This will store the reverse of the number
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        print(reverse)
        return reverse
s=Solution()   
s.isPalindrome(2332)

s.isPalindrome(852255665563451)