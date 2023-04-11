# Sort an array of 0,1,2 without any sorting algorithm. Complexity O(n) and space complexity O(1)

# function to sort array
# def arr012(a, arr_size):
#     lo = 0
#     hi = arr_size - 1 
#     mid = 0

#     Iterate till all items are sorted
#     while mid<=hi:
#         if element is 0
#         if a[mid]==0:
#             a[lo],a[mid] = a[mid],a[lo]
#             lo = lo + 1
#             mid = mid + 1
#         elif a[mid]==1:
#             mid = mid + 1
#         else:
#             a[mid],a[hi] = a[hi],a[mid]
#             hi = hi - 1

#     return a

# def printArray(a):
#     for k in a:
#         print(k,end = ' ')

# Driver program
# arr = [0,1,1,2,0,0,2,1,2,0,1]
# arr_size = len(arr)
# arr = arr012(arr,arr_size)
# printArray(arr)


#Doing the same problem with count

