a = [2*n-1 for n in range(100)]
b = [2**n for n in range(10)]
for n in b:
    a. append(n)
a = set(a)
a = list(a)
a. sort()
s = 0
for n in range(len(a)):
    s += a[n]
    if s > 12*a[n+1]:
        print("The answer is ", n)
        break

