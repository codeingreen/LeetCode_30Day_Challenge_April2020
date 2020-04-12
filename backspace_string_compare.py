class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def compact_string(string):
            
            list_string = list(string)
            result = []
            
            for item in list_string:
                if item != '#':
                    result.append(item)
                elif item == '#':
                    if len(result) > 0:
                        result[-1] != '#'
                        result.pop()
                        
            result = [x for x in result if x!='#']
            return ''.join(result)
        
        S_new = compact_string(S)
        T_new = compact_string(T)
        
        print(S_new, T_new)
        
        if S_new == T_new:
            return True
        
        return False
