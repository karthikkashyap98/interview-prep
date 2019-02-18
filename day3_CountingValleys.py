 #!/bin/python3


# Complete the countingValleys function below.
def countingValleys(n, s):
    sea=0
    ans=0
    for i in s:
        if i == 'U':
            sea=sea+1
        if i == 'D':
            sea=sea-1
        if sea == 0 and i=='U':
            ans = ans+1
    return ans

    

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)


