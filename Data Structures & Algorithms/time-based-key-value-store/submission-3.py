class TimeMap:

    def __init__(self):
        # store the values in an array in order of timestamp
        # when storing one we need to search through the array
        # when getting do a binary serach for the key, if not there return the -1 
        self.h = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.h.get(key):
            self.h[key] = [(value, timestamp)]
        else:
            self.h[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.h.get(key):
            return ""

        l, r = 0, len(self.h[key]) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if timestamp == self.h[key][m][1]:
                return self.h[key][m][0]
            
            if timestamp < self.h[key][m][1]:
                r = m - 1
            else:
                l = m + 1
        
        if l - 1 < 0: return ""

        return self.h[key][l - 1][0]

        

