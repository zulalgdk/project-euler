number = []

for i in range(999, 99, -1):

    for j in range(999, 99, -1):

        multiple = i * j

        mult = str(multiple)

        if(mult[0:] == mult[::-1]):

            number.append(int(mult))

print(max(number))
