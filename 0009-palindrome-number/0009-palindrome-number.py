class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 負數，或者個位數是 0 但本身不是 0 的數字，不可能是迴文
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        # 當原始數字大於反轉數字時，持續迴圈
        while x > reverted_number:
            # 將 x 的最後一位數加到 reverted_number 的末尾
            reverted_number = reverted_number * 10 + x % 10
            # 將 x 的最後一位數移除
            x //= 10
            
        # 迴圈結束時，如果數字長度是偶數，x 會等於 reverted_number (例如 1221 -> x=12, rev=12)
        # 如果是奇數，reverted_number 的長度會多一位 (例如 12321 -> x=12, rev=123)
        # 此時需要將 reverted_number 除以 10 來去掉中間的數字
        return x == reverted_number or x == reverted_number // 10