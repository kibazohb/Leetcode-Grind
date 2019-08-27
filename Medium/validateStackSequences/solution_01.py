class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        myStack = []
        j = 0
        for i in pushed:
            #this is where the pushing happens
            myStack.append(i)
            while myStack and j < len(popped) and myStack[-1] == popped[j]:
                myStack.pop()
                j+=1
            
        return len(myStack) == 0  
            
         
            
