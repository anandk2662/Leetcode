class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        List=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique=set()
        for word in words:
            code=""
            for j in range(len(word)):
                code+=List[ord(word[j])-97]
            unique.add(code)
        
        return len(unique)