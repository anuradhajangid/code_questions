#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = deque()
        operators = ["+", "-", '/', "*"]
        for char in tokens:
            if not mystack and char in operators:
                raise TypeError()
            if char not in operators:
                mystack.append(int(char))
            else:
                elementtop = mystack.pop()
                elementbottom = mystack.pop()
                if (char == "+"):
                    mystack.append(elementtop + elementbottom)
                elif char == "-":
                    mystack.append(elementbottom - elementtop)
                elif char == "/":
                    mystack.append(int(elementbottom / elementtop))
                elif char == "*":
                    mystack.append(elementbottom * elementtop)
                
        return mystack.pop()

        