
sum1 = 0
sum2 = 0
for i in range(1,101):
  us = pow(i,2)
  sum1 += us

for j in range(1,101):
  sum2 += j
  result= sum2**2
print ("sonuç=",result-sum1)
