class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):
	    
	    A = sorted(A)
	    
	    len_A = len(A)
	    
	    i = 0
	    j = 1
	    
	    while i<len_A and j<len_A:
	        
	        A[i],A[j] = A[j],A[i]
	        
	        i = i+2
	        j = j+2
	        
	    return A
