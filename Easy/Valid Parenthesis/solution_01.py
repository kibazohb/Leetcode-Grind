class Solution(object):
    def isValid(self, x):
        p_dict = {')':'(','}':'{',']':'['}
        myStack = []
        for element in x:
            if element in p_dict.values():
                myStack.append(element)
            else: 
                if not (myStack) or myStack.pop() != p_dict[element]:
                    return False
            
             
        if not (myStack):
            return True
        else:
            return False
