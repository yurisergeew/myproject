import math
sumBefore = float(input('сумма ='))
procent = float(input('годовой процент ='))
numYears = int(input('сколько лет прошло ='))
eps = float(input('eps ='))

sumAfter = sumBefore
An = 1.0
n = 1

while (sumAfter <= 800) :
    if (sumAfter > 800) :
        pass
    else (
    An = ((-1)**(n+1)) / float(((2*n-1)*(3**(n-1))))
#    print ('сколько набежало  = ', "{:8.5f}".format(sumAfter))
    print ('An = ', An)
    procent = procent + abs(An)
    for i in range(1,numYears+1):
        sumAfter = sumAfter + (sumAfter*procent)/100.0
    n = n+1)
print ('наши денюжки = ', "{:8.2f}".format(sumAfter))
print ('наш процент = ', "{:8.2f}".format(procent))
