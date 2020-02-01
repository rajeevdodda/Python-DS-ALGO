class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        else:
            str_num = str(x)
            length = len(str_num)
            for i in range(length//2):
                if str_num[i] != str_num[length - 1 - i]:
                    return False
            else:
                return True

s = Solution()

print(s.isPalindrome(000))

