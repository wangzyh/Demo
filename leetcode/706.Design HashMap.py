# Design a HashMap without using any built-in hash table libraries. 
# 
#  To be specific, your design should include these functions: 
# 
#  
#  put(key, value) : Insert a (key, value) pair into the HashMap. If the value a
# lready exists in the HashMap, update the value. 
#  get(key): Returns the value to which the specified key is mapped, or -1 if th
# is map contains no mapping for the key. 
#  remove(key) : Remove the mapping for the value key if this map contains the m
# apping for the key. 
#  
# 
#  
# Example: 
# 
#  
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1 
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found) 
#  
# 
#  
# Note: 
# 
#  
#  All keys and values will be in the range of [0, 1000000]. 
#  The number of operations will be in the range of [1, 10000]. 
#  Please do not use the built-in HashMap library. 
#  
#  Related Topics Hash Table Design 
#  👍 1224 👎 139

# region time
# 2021-01-17 20:45:41
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.get(key) != -1:
            self.hash_map.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    hashMap = MyHashMap()
    print(hashMap.put(1, 1))
    print(hashMap.put(2, 2))
    print(hashMap.get(1))  # returns    1
    print(hashMap.get(3))  # returns - 1(not found)
    print(hashMap.put(2, 1))  # update    the    existing    value
    print(hashMap.get(2))  # returns    1
    print(hashMap.remove(2))  # remove    the    mapping    for 2
    print(hashMap.remove(12))
    print(hashMap.get(2))  # returns - 1(not found)
