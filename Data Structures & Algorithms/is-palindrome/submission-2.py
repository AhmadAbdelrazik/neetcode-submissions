class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanse = ""
        for ch in s:
            if ch.isalnum():
                cleanse += ch
        
        print(cleanse)
        i, j = 0, len(cleanse)-1
        while i < j:
            if cleanse[i].lower() != cleanse[j].lower():
                return False
            i += 1
            j -= 1
        
        return True