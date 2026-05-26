class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        n = len(s)
        j = 0
        i = 0

        while j < n:
            if s[j] not in seen:
                seen.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1

            else:
                if s[i] in seen:
                    seen.remove(s[i])
                i += 1
        return ans