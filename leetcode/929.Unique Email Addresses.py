# Every email consists of a local name and a domain name, separated by the @ sig
# n. 
# 
#  For example, in alice@leetcode.com, alice is the local name, and leetcode.com
#  is the domain name. 
# 
#  Besides lowercase letters, these emails may contain '.'s or '+'s. 
# 
#  If you add periods ('.') between some characters in the local name part of an
#  email address, mail sent there will be forwarded to the same address without do
# ts in the local name. For example, "alice.z@leetcode.com" and "alicez@leetcode.c
# om" forward to the same email address. (Note that this rule does not apply for d
# omain names.) 
# 
#  If you add a plus ('+') in the local name, everything after the first plus si
# gn will be ignored. This allows certain emails to be filtered, for example m.y+n
# ame@email.com will be forwarded to my@email.com. (Again, this rule does not appl
# y for domain names.) 
# 
#  It is possible to use both of these rules at the same time. 
# 
#  Given a list of emails, we send one email to each address in the list. How ma
# ny different addresses actually receive mails? 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","t
# estemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually r
# eceive mails
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= emails[i].length <= 100 
#  1 <= emails.length <= 100 
#  Each emails[i] contains exactly one '@' character. 
#  All local and domain names are non-empty. 
#  Local names do not start with a '+' character. 
#  
#  
#  Related Topics String 
#  👍 1070 👎 207

# region time
# 2021-01-23 14:00:05
# endregion

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numUniqueEmails(self, emails) -> int:
        res = set()
        for i in emails:
            i = i[:i.index('@')].replace('.', '') + i[i.index('@'):]
            if '+' in i:
                i = i.replace(i[i.index('+'):i.index('@')], '')
            res.add(i)
        return len(res)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(n))
