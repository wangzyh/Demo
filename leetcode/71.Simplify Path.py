# Given a string path, which is an absolute path (starting with a slash '/') to 
# a file or directory in a Unix-style file system, convert it to the simplified ca
# nonical path. 
# 
#  In a Unix-style file system, a period '.' refers to the current directory, a 
# double period '..' refers to the directory up a level, and any multiple consecut
# ive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any
#  other format of periods such as '...' are treated as file/directory names. 
# 
#  The canonical path should have the following format: 
# 
#  
#  The path starts with a single slash '/'. 
#  Any two directories are separated by a single slash '/'. 
#  The path does not end with a trailing '/'. 
#  The path only contains the directories on the path from the root directory to
#  the target file or directory (i.e., no period '.' or double period '..') 
#  
# 
#  Return the simplified canonical path. 
# 
#  
#  Example 1: 
# 
#  
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory nam
# e.
#  
# 
#  Example 2: 
# 
#  
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the roo
# t level is the highest level you can go.
#  
# 
#  Example 3: 
# 
#  
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced 
# by a single one.
#  
# 
#  Example 4: 
# 
#  
# Input: path = "/a/./b/../../c/"
# Output: "/c"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= path.length <= 3000 
#  path consists of English letters, digits, period '.', slash '/' or '_'. 
#  path is a valid absolute Unix path. 
#  
#  Related Topics String Stack 
#  👍 313 👎 92

# region time
# 2021-04-05 22:31:00
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        q = []
        for p in path:
            if not p or p == '.':
                continue
            elif p == '..':
                if q:
                    q.pop()
            else:
                q.append(p)
        return '/' + '/'.join(q)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # n = '/a/./b/../../c/'
    n = "/a//b////c/d//././/.."
    print(Solution().simplifyPath(n))
