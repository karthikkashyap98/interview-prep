''''



Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format
The first line contains the first integer, . The second line contains the second integer, .
Output Format
Print the three lines as explained above.



'''



def repeatedString(s, n):
    count=s.count("a")
    mod=count*(n//len(s))
    final_count=mod+s[:n % len(s)].count("a")
    print(final_count)

n=int(input('enter a number'))
s=input('enter string to repeat')
repeatedString(s,n)
main()