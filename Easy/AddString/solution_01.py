class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #no leading zeroes
        j = len(num2) - 1
        i = len(num1) - 1
        ans = []
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                
                carry += int(num1[i]) + int(num2[j])
                if carry < 10:
                    ans.append(str(carry))
                    carry = 0
                else:
                    ans.append(str(carry%10))
                    carry = carry // 10

                i-=1
                j-=1
                
            elif j >= 0:
                carry += int(num2[j])

                if carry < 10:
                    ans.append(str(carry))
                    carry = 0
                else:
                    ans.append(str(carry%10))
                    carry = carry // 10

                j-=1


            elif i >= 0:
                carry += int(num1[i])

                if carry < 10:
                    ans.append(str(carry))
                    carry = 0
                else:
                    ans.append(str(carry%10))
                    carry = carry // 10

                i-=1
            
        if carry:
            ans.append(str(carry))
            
        ans = "".join(ans)
        return ans[::-1]
