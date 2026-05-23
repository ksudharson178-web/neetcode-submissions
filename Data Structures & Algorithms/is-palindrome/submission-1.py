class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""
        for i in s:
            if i.isalnum():
                c=c+i.lower()
        if c==c[::-1]:
            return True
        else:
            return False