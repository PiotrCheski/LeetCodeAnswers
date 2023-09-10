from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop()+stack.pop())
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(b//a)
            else:
                stack.append(int(c))

        return stack[-1]
    

    
tokens = ["2","1", "+"]
print(Solution().evalRPN(tokens))