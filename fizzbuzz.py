

intList = list(range(1,101))
newList = []
for c,i in enumerate(intList):
    if i%15==0:
        intList[c] = 'FizzBuzz'
    elif i%3==0:
        intList[c] = 'Fizz'
    elif i%5==0:
        intList[c] = 'Buzz'

print(intList)
