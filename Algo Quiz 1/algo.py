a = [123, 13, 456 ,21]
min1 = a[0]
min2 = min1
min3 = min1
min4 = min1

for i in range(len(a) -1):   
    if a[i] > a[i+1]:
        if min1 > a[i+1]:
            min4 = min3
            min3 = min2
            min2 = min1
            min1 - a[i+1]

        elif min2 > a[i+1]:
            min4 = min3
            min3 = min2
            min2 = a[i+1]

        elif min3 > a[i+1]:
            min4 = min3
            min3 = a[i+1]

        elif min4 > a[i+1]:
            min4 = a[i+1]

print(min4) 
