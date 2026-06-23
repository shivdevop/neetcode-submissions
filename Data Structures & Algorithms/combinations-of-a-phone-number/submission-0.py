from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        hash_map={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        res=[]
        temp=[]

        def dfs(ind):
            if ind==len(digits):
                res.append("".join(temp[:]))
                return

            for c in hash_map[digits[ind]]:
                temp.append(c)
                dfs(ind+1)
                temp.pop()

        dfs(0)
        return res        
