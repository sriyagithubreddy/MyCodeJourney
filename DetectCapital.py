class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        result=word.isupper() or (word[0].isupper() and word[1:].islower()) or word.islower()
        return result