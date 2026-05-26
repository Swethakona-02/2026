from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        freq = Counter(word)
        count = 0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if freq[ch] > 0 and freq[ch.upper()] > 0:
                count += 1
        return count
