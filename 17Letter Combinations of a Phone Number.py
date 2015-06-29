##Letter Combinations of a Phone Number
##Given a digit string,
##return all possible letter combinations that the number could represent.
##
##2015年6月29日  AC
##zss

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        digitsMap={'2':['a','b','c'],
                   '3':['d','e','f'],
                   '4':['g','h','i'],
                   '5':['j','k','l'],
                   '6':['m','n','o'],
                   '7':['p','q','r','s'],
                   '8':['t','u','v'],
                   '9':['w','x','y','z'],
                   '1':[],'0':[]}
        result = []
        for i in digits:
            result = self.mass(result,digitsMap[i])
        return result

    def mass(self,lista,listb):
        if not lista:return listb
        if not listb:return lista
        result = []
        for a in lista:
            for b in listb:
                result.append(''.join([a,b]))
        return result
