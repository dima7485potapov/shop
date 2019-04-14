n = 0
a = [[1]]

while n < 20:
    b = [1]
    m = 0
    for i in range(1, len(a[n])):
        k = a[n][i-1]+a[n][i]
        b.append(k)
        if k%2 != 0:
            m+=1
    print(m)
    print(b)
    print("")
    b.append(1)
    
    a.append(b)
    n+=1

