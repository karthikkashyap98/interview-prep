'''
Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


Output

Berry
Harry

'''



if __name__ == '__main__':
    student = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        marks.append(score) 
    marks.sort()
    student.sort()
    mini = min(marks)
    for i in marks:
        if i-mini ==0:
            pass
        else:
            a = i
            break
    for k in student:
        if k[1] == a:
            print(k[0])         
