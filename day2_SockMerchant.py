'''
Input Format

The first line contains an integer n, the number of socks represented in ar. 
The second line contains n space-separated integers describing the colors arr[i] of the socks in the pile.


Output Format

Return the total number of matching pairs of socks that John can sell.
'''

def sockMerchant(n, ar):

    count = 0 
    c = set(ar)
    for x in c:
        count = count + ar.count(x)//2 

    return count    

if __name__ == '__main__':
    
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
