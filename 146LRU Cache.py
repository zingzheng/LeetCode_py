##LRU Cache
##Design and implement a data structure for Least Recently Used (LRU) cache.
##It should support the following operations: get and set.
##get(key) - Get the value (will always be positive) of the key if the key exists
##in the cache, otherwise return -1.
##set(key, value) - Set or insert the value if the key is not already present.
##When the cache reached its capacity, it should invalidate the least recently
##used item before inserting a new item.
##
##2015年9月22日 11:27:34  AC
##zss

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dic={}
        self.cacahe=[]
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            self.set(key,self.dic[key])
            return self.dic[key]
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self.cacahe.remove(key)
        else:
            if len(self.cacahe)>=self.cap:
                self.dic.pop(self.cacahe.pop(-1))
        self.dic[key]=value
        self.cacahe.insert(0,key)
        print(self.cacahe,self.dic)
            
            
            
