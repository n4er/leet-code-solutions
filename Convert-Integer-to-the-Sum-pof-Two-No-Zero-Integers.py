class Solution(object):
    def getNoZeroIntegers(self, n):
        for a in range (1,n):
            b = n-a
            if not self.has_zero(a) and not self.has_zero(b):
                return [a,b]
    
    def has_zero(self, num):
        return '0' in str(num)        