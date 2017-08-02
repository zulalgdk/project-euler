def fibonacci(limit):

    numbers = [1, 2]

    x = numbers[0] + numbers[1]

    while x < int(limit):

        x = (int(numbers[len(numbers)-1])+int(numbers[len(numbers)-2]))

        if(x < int(limit)):
            
            numbers.append(y)

    return(numbers)


def addition(num):

    sum = 0

    numbers = fibonacci(num)

    for i in range(len(numbers)):

        if(numbers[i] % 2 == 0):

            sum += numbers[i]

    print(sum)

addition(4000000)
