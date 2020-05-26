#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#

# @lc code=start
import re
class Solution:
    def countAndSay(self, n: int) -> str:
        start_str = "1"
        for i in range(n-1):
            next_str=""
            while start_str:
                re_obj = re.match('({}*)(.*)'.format(start_str[0]), start_str)
                next_str += '{}{}'.format(len(re_obj.group(1)), start_str[0])
                start_str = re_obj.group(2)
            start_str = next_str
        return start_str
# @lc code=end

