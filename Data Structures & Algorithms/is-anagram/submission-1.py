class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        c = set(s)
        for i in c:
            if s.count(i) != t.count(i):
                return False
        return True
