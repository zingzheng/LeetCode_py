##Count and Say
##The count-and-say sequence is the sequence of integers beginning as follows:
##1, 11, 21, 1211, 111221, ...
##1 is read off as "one 1" or 11.
##11 is read off as "two 1s" or 21.
##21 is read off as "one 2, then one 1" or 1211.
##Given an integer n, generate the nth sequence.
##Note: The sequence of integers will be represented as a string.
##
##2015年7月4日   AC
##zss
##
class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if not n:return
        strn = str(n)
        result = '1'
        for i in range(n,1,-1):
            result = self.countPre(result)
        return result

    def countPre(self, pre):
        result,count='',1
        for i in range(1,len(pre)+1):
            if i == len(pre) or pre[i] != pre[i-1]:
                result = ''.join([result,str(count),pre[i-1]])
                count = 1
            else:
                count += 1
        return result
