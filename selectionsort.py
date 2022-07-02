def findsamllest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range (1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
            
    return smallest_index

def selectionsort(arr):
    selarr=[]
    for i in range(len(arr)):
        small=findsamllest(arr)
        selarr.append(arr.pop(small))
        
    return selarr
            
arrays=[4,2,5,6,8,90,1,3]
print(selectionsort(arrays))
#print(findsamllest(arrays))