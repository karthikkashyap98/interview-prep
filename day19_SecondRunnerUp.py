'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given scores. Store them in a list and find the score of the runner-up.
Sample Input 0
5
2 3 6 6 5
Sample Output 0
5

'''


n=int(input('enter n'))
list1=[]
arr = map(int, input('enter array').split())
for j in arr:
    if j not in list1:
        list1.append(j)
list1.remove(max(list1))
print(max(list1))