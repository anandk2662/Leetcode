class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        vowels=""
        for i in s:
            if i.lower() in "aeiou":
                vowels+=i
        reverseVowels=vowels[::-1]
        idx=0
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                s[i]=reverseVowels[idx]
                idx+=1

        return "".join(s)