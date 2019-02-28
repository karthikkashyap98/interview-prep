# Bubble sort with recursion
# try and except is used to eliminate IndexError 
# when it goes out of range




def bubble_sort(listt): 
    for i, num in enumerate(listt): 
        try: 
            if listt[i+1] < num: 
                listt[i] = listt[i+1] 
                listt[i+1] = num 
                bubble_sort(listt) 
        except IndexError: 
            pass
    return listt 
  
listt = [641, 343, 252, 121, 224, 117, 90] 
bubble_sort(listt) 
  
print("Sorted array:"); 
for i in range(0, len(listt)): 
    print(listt[i], end=' ') 