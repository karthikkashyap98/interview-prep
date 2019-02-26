'''
Input

The first line contains two integers, n and k, the number of priced toys and the amount Mark has to spend. 
The next line contains n space-separated integers prices[i]




Output 

An integer that denotes the maximum number of toys Mark can buy for his son.


'''

def maximumToys(prices, k):
    prices.sort()
    sum = 0
    count = 0
    for i in prices:
        sum = sum + i
        if sum <= k:
            count = count +1

    return count         

if __name__ == '__main__':
    

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)