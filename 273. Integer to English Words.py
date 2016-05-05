##273. Integer to English Words
##Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
##
##2016年3月6日 16:58:13
##zss


class Solution(object):

    one_nine=['0','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    ten_nineteen=['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    twenty_ninety=['0','0','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    unit=['','Thousand','Million','Billion','Trillion']
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num,i,res = str(num),0,''
        res=[]
        while True:
            temp = self.three(int(num[-3:]))
            if temp:
                if i!=0:
                    res.append(self.unit[i])
                res.append(temp)
            if len(num)<=3:break
            num = num[:-3]
            i+=1
        return 'Zero' if not res else ' '.join(res[::-1])
        

    def three(self,num):
        res = ""
        if num//100>0:
            res = ' '.join([res,self.one_nine[num//100],'Hundred'])
            num%=100
        if 10<=num<=19:
            res = ' '.join([res,self.ten_nineteen[num-10]])
        elif num>=20:
            res = ' '.join([res,self.twenty_ninety[num//10]])
            num%=10
        if 0<num<10:
            res = ' '.join([res,self.one_nine[num]])
        return res[1:]

            
            
            
