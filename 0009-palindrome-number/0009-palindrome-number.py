class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 負數不可能是迴文
        if x < 0:
            return False
        
        # 將整數轉為字串，然後比較字串與其反轉後是否相等
        return str(x) == str(x)[::-1]