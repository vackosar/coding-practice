class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force: search all substrings and check if they are palindromic N**3
        # all substrings = N**2, comparison with reversal is N as strings lenght ~N
        # complexity N ** 2

        # there are much better solutions. Linear time solution possible with a suffix tree for s + "#" rs
        # there is even much faster N**2 solution than this

        rs = ''.join(c for c in reversed(s))
        max_s = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                ri = len(s) - i
                rj = len(s) - j
                if len(max_s) >= j - i:
                    break

                vs = s[i:j]
                rvs = rs[rj: ri]
                if vs == rvs:
                    max_s = vs
                    break

        return max_s

assert Solution().longestPalindrome( "ac") == "a"
assert Solution().longestPalindrome( "babad") == "bab"
