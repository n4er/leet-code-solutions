class Solution(object):
    def findLucky(self, arr):
        freq = {}
        
        # count frequencies
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        res = -1
        # check lucky condition
        for num, count in freq.items():
            if num == count:
                res = max(res, num)
        
        return res