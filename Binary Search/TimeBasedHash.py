class TimeMap(object):

    def __init__(self):
        self.hashMap = {}
        

    def set(self, key, value, timestamp):
        
        if key in self.hashMap.keys():
            self.hashMap[key].append([value, timestamp])
        else:
            self.hashMap[key] = [[value,timestamp]]
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res, values = "", self.hashMap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)