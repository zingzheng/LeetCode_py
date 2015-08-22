##Repeated DNA Sequences
##All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
##for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
##Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
##
##2015年8月19日 10:58:12  AC
##zss

class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        dic={}
        result=[]
        if len(s)<11:return result
        for i in range(len(s)-9):
            tmp=s[i:i+10]
            if tmp not in dic:
                dic[tmp]=1
            else:
                if dic[tmp]==1:
                    result.append(tmp)
                dic[tmp]+=1
        return result
