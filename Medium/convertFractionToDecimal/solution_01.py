class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        #attain sign
        if not numerator:
            return "0"
        out = []
        sign = 1
        if numerator < 0:
            sign = sign * -1
            numerator *= - 1
        if denominator < 0:
            sign = sign * -1
            denominator *= - 1
        
        if sign == -1:
            out.append("-")
        
        if numerator > denominator:
            num = numerator // denominator
            rem = numerator % denominator
            out.append(str(num))
            numerator = rem
        else:
            out.append("0")
            
        if numerator:
            out.append(".")
        cache = {}
        index = len(out)
        while numerator:
            if numerator in cache:
                out.insert(cache[numerator], "(")
                out.append(")")
                return "".join(out)
                
            
            cache[numerator] = index
            numerator *= 10
            num = numerator // denominator
            numerator = numerator % denominator
            out.append(str(num))
            index += 1
            
        return "".join(out)  
