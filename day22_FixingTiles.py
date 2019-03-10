def solve(s):
    for i in range(len(s)):
        s=s.title()
    print(s)
def main():
    s=input('enter string')
    solve(s)
main()