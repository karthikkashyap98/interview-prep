'''You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. 
You need to find the minimum number of swaps required to sort the array in ascending order.'''


n = int(input("enter the number of elements"))
arr = list(map(int, input().split("enter the list")))
swaps = 0

for i in range(0, n - 1):
    while arr[i] != i + 1:
        temp = arr[arr[i] - 1]
        arr[arr[i] - 1] = arr[i]
        arr[i] = temp
        swaps += 1

print(swaps)