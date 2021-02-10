# You have a RecentCounter class which counts the number of recent requests with
# in a certain time frame. 
# 
#  Implement the RecentCounter class: 
# 
#  
#  RecentCounter() Initializes the counter with zero recent requests. 
#  int ping(int t) Adds a new request at time t, where t represents some time in
#  milliseconds, and returns the number of requests that has happened in the past 
# 3000 milliseconds (including the new request). Specifically, return the number o
# f requests that have happened in the inclusive range [t - 3000, t]. 
#  
# 
#  It is guaranteed that every call to ping uses a strictly larger value of t th
# an the previous call. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]
# 
# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], retur
# n 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], re
# turn 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,300
# 2], return 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= t <= 109 
#  Each test case will call ping with strictly increasing values of t. 
#  At most 104 calls will be made to ping. 
#  
#  Related Topics Queue 
#  👍 538 👎 2101

# region time
# 2021-02-07 21:08:50
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class RecentCounter:
    # count = []

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        # if not self.count:
        #     self.count.append([t])
        #     return len(self.count)
        # for i in range(len(self.count[-1])):
        #     if self.count[-1][-1] + 3000 < t:
        #         self.count.append([t])
        #         break
        #     if self.count[-1][i] + 3000 >= t:
        #         self.count.append(self.count[-1][i:])
        #         self.count[-1].append(t)
        #         break
        # return len(self.count[-1])
        self.q.append(t)
        while self.q[0] + 3000 < t:
            self.q.pop(0)
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # ["RecentCounter", "ping", "ping", "ping", "ping"]
    # [[], [1], [100], [3001], [3002]]
    # [642], [1849], [4921], [5936], [5957]
    rec = RecentCounter()
    print(rec.ping(642))
    print(rec.ping(1849))
    print(rec.ping(4921))
    print(rec.ping(5936))
    print(rec.ping(5957))
