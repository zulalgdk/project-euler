def xy():
    c=5
    sum=3+4+5
    while (c < sum ):
        for b in range (4,c):
            for a in range (3,b):
                if (a**2 + b**2 == c**2):
                    if 1000 % (a + b + c) == 0:
                        x= (1000 / ( a + b + c) )
                        mult = ( a * x * b * x * c * x )
                        return mult
        c+=1
        sum =a+b+c

print(xy())
