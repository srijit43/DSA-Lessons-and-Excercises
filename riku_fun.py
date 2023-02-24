def riku_square(n):
    if (n==1):
        return n
    else:
        return((2*n-1) + riku_square(n-1))


inp = int(input("Enter number to be squared:")) #Number must be greater than 0
if inp > 1:
    print("The square of", inp, "is", riku_square(inp))

print("Ok")