class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.lower()
        t.lower()
        list1=list(s)
        list2=list(t)
        list1.sort()
        list2.sort()
        if(list1==list2):
            return True
        return False            
