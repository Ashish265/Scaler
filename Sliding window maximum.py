class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
	    from collections import deque
	    
        N = len(A)
        i = j = 0
        
        max_q = deque()
        max_w = []
        while j < N:
            # Keep track of monotonically "decreasing" max values.
            while max_q and A[j] > max_q[-1]:
                max_q.pop()
        
            max_q.append(A[j])
        
            # Once expanded to the size of the window k, start recording max values and shifting window.
            if j - i + 1 == B:
                max_w.append(max_q[0])
        
                # Shifted past the first max, pop it off.
                if max_q[0] == A[i]:
                    max_q.popleft()
        
                i += 1
        
            j += 1
        
        return max_w