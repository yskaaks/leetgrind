class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        def helper(m):
            if m == 0:
                return [""]
            if m == 1:
                return ["0","1","8"]
            
            prev = helper(m-2)
            curr = []
            for num in prev:
                if m != n:
                    curr.append("0" + num + "0")  
                curr.append("1" + num + "1")
                curr.append("6" + num + "9")
                curr.append("8" + num + "8")
                curr.append("9" + num + "6")
            return curr
        return helper(n)