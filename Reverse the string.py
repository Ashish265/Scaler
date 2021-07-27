class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        
        A = A.split()
        
        A = A[::-1]
        
        return " ".join(A).strip()
        