class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s, lst_t = list(s), list(t)
        lst_s.sort()
        lst_t.sort()

        if lst_s == lst_t:
            return True
        else:
            return False


        