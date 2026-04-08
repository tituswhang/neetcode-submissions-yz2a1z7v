class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) > 0:
                top = stack[-1]

                match c:
                    case ')':
                        if top == '(':
                            stack.pop()
                            continue
                    case '}':
                        if top == '{':
                            stack.pop()
                            continue
                    case ']':
                        if top == '[':
                            stack.pop()
                            continue

            stack.append(c)

        if len(stack) != 0:
            return False
        
        return True