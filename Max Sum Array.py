def max_sum_array(arr):
    
    max_so_far = float("-inf")
    maxEndingHere = 0
    
    start =0
    end =0
    
    beg = 0
    
    for i in range(len(arr)):
        
        maxEndingHere = maxEndingHere + arr[i]
        
        if maxEndingHere < arr[i]:
            maxEndingHere = arr[i]
            beg =i
            
        if max_so_far < maxEndingHere:
            max_so_far = maxEndingHere
            start = beg
            end = i
    return arr[start:end+1]