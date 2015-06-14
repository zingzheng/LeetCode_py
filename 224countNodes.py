##Basic Calculator
##Implement a basic calculator to evaluate a simple expression string.
##The expression string may contain open ( and closing parentheses ),
##the plus + or minus sign -, non-negative integers and empty spaces
##
##2015年6月9日 AC
##zss

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        result = 0
        nums = []
        ops = []
        if not s:
            return 0

        tmps = s.replace(' ', '')
        i=0
        while i < len(tmps):
            #数字处理
            if tmps[i] not in('+','-','(',')'):
                numstr=[]
                while i < len(tmps)  and tmps[i] not in ('+','-','(',')'):
                    numstr.append(tmps[i])
                    i += 1
                    ttt = ''.join(numstr)
                i -= 1
                nums.append(ttt)
            #+，-，）
            elif tmps[i] in('+','-',')'):
                #若操作栈中有非（的操作，出栈计算
                if ops and ops[-1] !='(':
                    num_a = int(nums.pop())
                    num_b = int(nums.pop())
                    op = ops.pop()
                    if op == '+':
                        result = num_b+num_a
                    else:
                        result = num_b-num_a
                    nums.append(result)
                #若操作栈中最后一个为)，新操作直接入栈
                if tmps[i] != ')':
                    ops.append(tmps[i])
                else:
                    ops.pop()
            #（直接进ops
            elif tmps[i] == '(':
                ops.append(tmps[i])
            i += 1

        #最后出栈    
        if ops:
            num_a = int(nums.pop())
            num_b = int(nums.pop())
            op = ops.pop()
            if op == '+':
                result = num_b+num_a
            else:
                result = num_b-num_a
        else:
            result = int(nums.pop())
        return result
            
                
                
