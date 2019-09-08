class Solution:
    def calculate(self, s: str) -> int:
        oprStack = []
        numStack = []
        nums = "0123456789"
        a , b = 0, 0
        i = 0
        j = 0
        digit = 0
        
        while i < len(s):
            if s[i] == " ":
                i+=1
            elif s[i] in nums:
                j = i
                #to get double digit and more numbers
                while j < len(s) and s[j] in nums:
                    j+=1
                digit = (s[i:j])
                #print(digit)
                #digit = int(digit)
                numStack.append(int(digit))
                i=j
            elif s[i] == "+" or s[i] == "-":
                while len(oprStack):
                    opr = oprStack[-1]
                    oprStack.pop()
                    a = numStack[-1]
                    numStack.pop()
                    b = numStack[-1]
                    numStack.pop()
                    if opr == "+":
                        numStack.append(b + a)
                    elif opr == "-":
                        numStack.append(b - a)
                    elif opr == "*":
                        numStack.append(b * a)
                    else:
                        numStack.append(b // a)
                
                oprStack.append(s[i])
                i+=1
            elif s[i] == "/" or s[i] == "*":
                while len(oprStack) and (oprStack[-1] == '/' or oprStack[-1] == '*'):
                    opr = oprStack[-1]
                    oprStack.pop()
                    a = numStack[-1]
                    numStack.pop()
                    b = numStack[-1]
                    numStack.pop()
                    if opr == "*":
                        numStack.append(b * a)
                    elif opr == "/":
                        numStack.append(b // a)
                oprStack.append(s[i])
                i+=1
                
        while len(oprStack):
            opr = oprStack[-1]
            oprStack.pop()
            a = numStack[-1]
            numStack.pop()
            b = numStack[-1]
            numStack.pop()
            if opr== "+":
                numStack.append(b + a)
            elif opr == "-":
                numStack.append(b - a)
            elif opr == "*":
                numStack.append(b * a)
            else:
                numStack.append(b // a)
                    
       
        ans = numStack[-1]
        return ans
        
        
                        
                    
                
                
                
                
            
            
        
        
        
