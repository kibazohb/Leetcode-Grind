class Solution:
    def expand(self, S: str) -> List[str]:
        """
        Google SWE intern interview type of qn
        "{a,b}c{d,e}f"
        Questions to ask: Will sequence of characters be in order?
        can we have more than one interfering character?
        can we have interfering characters at the beginning of the string?
        """
        inside_char = []
        out = [""]
        access = False
        for x in S:
            if x == "{":
                access = True
                
            elif x == ",":
                continue
            elif x == "}":
                access = False
                out = [j + i for i in inside_char for j in out]
                inside_char = []
                
            elif access:
                inside_char.append(x)
            else:
                out = [char + x for char in out]
                
               
        return sorted(out) 
