class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        d=0
        for i in nums:
            if i in s:
                d+=1
            s.add(i)
        if d>0:
            return True
        else:
            return False