# Perform Linear search to find a given element in the array 


def search(ar, n, x): 
  
    for i in range (0, n): 
        if (ar[i] == x): 
            return i; 
    return -1; 
  
# Main program
ar = [ 2, 3, 4, 10, 40 ]; 
x = 10; 
n = len(ar); 
result = search(ar, n, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result); 
