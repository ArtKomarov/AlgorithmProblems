
class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {
            "(": ")",
            "[": "]",
            "{": "}",
            }
        stack = []
        for c in s:
            if c in parantheses.keys():
                stack.append(c)
            elif c in parantheses.values():
                try:
                    last = stack.pop()
                except IndexError:
                    return False
                if parantheses[last] != c:
                    return False
            else:
                return False
            
        return len(stack) == 0
