class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b == ')':
                if not (stack and stack[-1] == '('):
                    return False
                stack.pop()
            elif b == '}':
                if not (stack and stack[-1] == '{'):
                    return False
                stack.pop()
            elif b == ']':
                if not (stack and stack[-1] == '['): #if not checks if false
                    return False
                stack.pop()
            else:
                stack.append(b)

        return len(stack) == 0
