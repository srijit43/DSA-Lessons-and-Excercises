# #given array
# a = {1,2,3}

# #destination array
# #a = {3,2,1}

# # Function to reverse A[] from start to end
# def reverseList(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1

# A = []
# n = int(input("Enter number of elements:"))
# # iterating till the range
# for i in range(0,n):
#     ele = int(input())
#     # adding the element
#     A.append(ele)

# print(A)

# x = len(A)

# reverseList(A, 0, x-1)
# print("Reversed list is")
# print(A)         

# Recursive manner

def revlist(A,start,end):
    if start>=end:
        return
    A[start],A[end] = A[end],A[start]
    revlist(A,start+1,end-1)

A = [1,2,3]
print(A)
revlist(A,0,2)
print(A)    
