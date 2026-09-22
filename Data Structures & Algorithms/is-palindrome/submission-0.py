import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
        return cleaned == cleaned[::-1]
