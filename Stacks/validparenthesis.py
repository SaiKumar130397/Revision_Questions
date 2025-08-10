class Solution:
    def isBalanced(s):
        stack = []
        tmp = {'}' : '{',
                ']' : '[',
                ')' : '('}
            
        for i in s:
            if i in ['[', '(', '{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if x != tmp[i]:
                    return False
        if len(stack) != 0:
            return False
            
        return True 