class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 負數，或者個位數是 0 但本身不是 0 的數字，不可能是迴文
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0

        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
            
        return x == reverted_number or x == reverted_number // 10