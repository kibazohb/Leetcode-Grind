class Solution:
    def removeDuplicates(self, S: str) -> str:
        #string of lowercase letters
        #remove adjacent duplicates
        #use stack, keep track of previous character
        stack = []
        for letter in S:
            
            if (len(stack) != 0) and stack[-1] == letter :
                    stack.pop()
            else:
                stack.append(letter)
             
        return "".join(stack)   
