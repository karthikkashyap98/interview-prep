'''

Emma is playing a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . 
She must avoid the thunderheads. 
Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. 
It is always possible to win the game.
For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. 
Input Format
The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .
Output Format
Print the minimum number of jumps needed to win the game.


'''

def jumpingclouds(c):
    jump=0
    i=0
    while i<len(c)-1:
        if (i+2<len(c) and c[i+2]!=1):
            i+=1
        jump+=1
        i+=1
    print(jump)

def main():
    n=int(input('Enter'))
    c=list(input('Enter'))
    jumpingclouds(c)
main()