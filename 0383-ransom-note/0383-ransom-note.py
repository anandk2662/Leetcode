class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        flag=False

        for i in ransomNote:
            if i in magazine and magazine.count(i)>=ransomNote.count(i):
                continue
            else:
                return False
        return True