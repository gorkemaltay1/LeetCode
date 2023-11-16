class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        if n<m:
            return sum(range(1,n+1))
        elif n==m:
            return int(sum(range(1,n)) - n)
        else:
            largest_divisible_num = 0
            for i in range(n,1,-1):
                if i%m==0:
                    largest_divisible_num = i
                    break
            divisible_sum=(((largest_divisible_num - m)/m)+1)*(largest_divisible_num + m)/2
            non_divisible_sum = sum(range(1,n+1)) - divisible_sum
            return int(non_divisible_sum - divisible_sum)
            