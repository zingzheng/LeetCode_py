##Count Primes
##Description:
##Count the number of prime numbers less than a non-negative number, n.
##
##2015年6月11日  AC
##zss

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime = [False]*n
        prime[2] = True
        count = 0
        for i in range(3,n,2):
            prime[i] = True

        for i in range(3,int(n**0.5)+1,2):
            if prime[i]:
                for j in range(i+i,n,i):
                    prime[j] = False

        for i in range(1,n):
            if prime[i]:
                count+=1
        return count
