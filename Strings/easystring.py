class Solution:
    def transform(S):
        S = S.lower()
        ans = ''
        cnt = 1
        char = S[0]
        for i in range(1, len(S)):
            if S[i] == char:
                cnt+= 1
            else:
                ans+= f'{cnt}' + char 
                char = S[i]
                cnt = 1
        ans+= f'{cnt}' + char
        return ans
        