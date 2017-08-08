sum=2

for i in range (3,2000001,2):
    for j in range (3,int(i**0.5)+1, 2):
        if i%j==0:
            break
    else:
       sum +=i
print(sum)
