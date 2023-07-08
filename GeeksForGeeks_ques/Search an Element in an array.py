def search(self,arr, N, X):
        #Your code here
        
        pos = -1
        
        for i in range(N):
            
            if arr[i] == X:
                pos = i
                
                return pos
        return pos
    

