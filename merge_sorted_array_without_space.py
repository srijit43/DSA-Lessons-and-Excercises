#Merge two sorted arrays without using extra space
#ex:{3,1,2},{1,5,4} gives result {1,1,2,3,4,5}

#Solution

def mergeArrays(arr1,arr2,n1,n2,arr3):
    i = 0
    j = 0
    k = 0

    while(i<n1):
        arr3[k] = arr1[i]
        k += 1
        i += 1

    while(j<n2):
        arr3[k] = arr2[j]
        k += 1
        j += 1

    arr3.sort()

#Driver Code

if __name__ == '__main__':
    a = [4,2,5,1]
    n1 = len(a)
    b = [7,6,3,8,4]
    n2 = len(b)

    c = [0 for i in range(n1+n2)]
    mergeArrays(a,b,n1,n2,c)

    print("Array after merging:")
    for i in range(n1 + n2):
        print(c[i],end = " ")

