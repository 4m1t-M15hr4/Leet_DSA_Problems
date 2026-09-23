class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
            
                if stack[-1] != ch[i]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

   
            

            
