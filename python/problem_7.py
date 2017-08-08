counter=1
i = 3
while (counter < 10001):
    for j in range(3, int(i**0.5)+1, 2):
        if (i % j == 0) :
            break
    else:
        counter += 1

    i += 2
print(i-2)
