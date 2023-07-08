class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        
        pos = -1
        
        for i in range(n):
            
            if arr[i] == k:
                pos = i
                
                return pos
                
        return pos

