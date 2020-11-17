def search(mat, x): 
    i = 0
    j = len(mat) - 1 #column length
    rowl = len(mat[0]) - 1 #row length
    
    while ( i < rowl and j >= 0 ): 
      
        if (mat[i][j] == x ): 
      
            print("n Found at (", i, ", ", j, ")") 
            return 1
      
        if (mat[i][j] > x ): 
            j -= 1
              
        else:  
            i += 1
      
    print("Element not found") 
    return 0
