class Solution:
    def romanToInt(self, s: str) -> int:
        RomanKey = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}
        answer = 0
        for i in range(len(s)):
            answer += RomanKey[s[i]]
            if(i > 0 and RomanKey[s[i]] > RomanKey[s[i-1]]):
                answer -= (2*RomanKey[s[i-1]])
        return answer
