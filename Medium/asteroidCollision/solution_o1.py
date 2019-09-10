class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        myStack = []
        myStack.append(asteroids[0])
        
        for i in range(1,len(asteroids)):
            safe = True
            while myStack and asteroids[i] < 0 < myStack[-1]:
                
                if abs(asteroids[i]) > myStack[-1]:
                    myStack.pop()
                
                elif abs(asteroids[i]) == myStack[-1]:
                    myStack.pop()
                    safe = False
                    break
                else:
                    safe = False
                    break
                    
                    
            if safe:
                myStack.append(asteroids[i])
        return myStack 
