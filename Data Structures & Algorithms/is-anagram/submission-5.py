class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = {}
        for letter in s:
            hash[letter] = hash.get(letter, 0) + 1
        
        for letter in t:
            if letter not in hash or hash[letter] == 0:
                return False
            else:
                hash[letter] -= 1

        return True