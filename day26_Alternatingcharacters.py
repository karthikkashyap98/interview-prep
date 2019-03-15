'''You are given a string containing characters  and  only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
For example, given the string , remove an  at positions  and  to make  in  deletions.
Input Format
The first line contains an integer , the number of queries. 
The next  lines each contain a string .
Output Format
For each query, print the minimum number of deletions required on a new line.'''



def alternatingcharacters(s):
    count=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1
    print(count)

def main():
    s=input('enter string')
    alternatingcharacters(s)
main()