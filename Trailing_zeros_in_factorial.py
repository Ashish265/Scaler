class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        
        x = A
        s=0
        x =x//5
        s += x
        
        while (x>=5):
            x=x//5
            s+=x
            
        return s