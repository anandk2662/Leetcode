class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomeNote=Counter(ransomNote)
        magazine=Counter(magazine)
        for key,val in ransomeNote.items():
            if magazine[key]<val:
                return False

        return True