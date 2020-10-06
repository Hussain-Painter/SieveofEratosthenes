def sieve(n):
    arr = [True] * n
    arr[0] = False
    arr[1] = False
    i = 2
    while i * i <= len(arr):
        if arr[i] == True:
            j = i * i
            while j < len(arr):
                arr[j] = False
                j = j + i
        i = i + 1
    for i in range(0,len(arr)):
        if arr[i] == True:
            print(i)

#driver code
n = int(input("Enter a number: "))
print("The prime numbers from 0 to", n,"are: ")
sieve(n + 1)

