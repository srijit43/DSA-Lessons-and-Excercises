# def move(arr):
#     arr.sort()

# a = [-3,2,1,4,-6,0]
# move(a)

# for e in a:
#     print(e,end = " ")

#The approach 1 has complexity O(nlogn)

#Approach 2

# def rearrange(arr,n):
#     j = 0                       #declare a pointer
#     for i in range(0,n):
#         if (arr[i]<0):          #if negative
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             j = j + 1           #increment pointer
#     print(arr)

# #Driver Code
# a = [-2,8,-4,-3,0,9,5]
# n = len(a)
# rearrange(a,n)

# #Complexity is O(N) linear and space is also O(1) linear

#We can fo this using dutcvh national flag as well

# def rearrange(arr,n):
#     low,high = 0,n-1
#     while(low<high):
#         if (arr[low]<0):
#             low += 1
#         elif(arr[high]>0):
#             high -= 1
#         else:
#             arr[low],arr[high] = arr[high],arr[low]


# def display_arr(arr,n):
#     for i in range(n):
#         print(arr[i],end = " ")

#     print('')

# #Driver Code
# a = [-3,-5,1,3,5,8,-9,7,-7,2]
# n = len(a)

# rearrange(a,n)
# display_arr(a,n)

#Same complexity as approach 2
