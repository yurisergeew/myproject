import math
from matplotlib import pyplot
sumBefore = float(input('сумма ='))
procent = float(input('годовой процент ='))
numYears = int(input('сколько лет прошло ='))
#eps = float(input('eps ='))

sumAfter = sumBefore
An = 1.0
n = 1
summ = []
year = []

def myfunc(n) :
        return ((-1)**(n+1)) / float(((2*n-1)*(3**(n-1))))

while (sumAfter <= 800) :
        sumBefore = sumAfter
        An = myfunc(n)
#       print ('сколько набежало  = ', "{:8.5f}".format(sumAfter))
#        print ('An = ', An)
        procent = procent + abs(An)
        for i in range(1,numYears+1):
            sumAfter = sumAfter + (sumAfter*procent)/100.0
            summ.append(sumAfter)
            year.append(i)
        n = n+1
#print ('наши денюжки = ', "{:8.2f}".format(sumBefore))
#print ('наш процент = ', "{:8.2f}".format(procent))

pyplot.plot(year[0:], summ[0:], color='magenta', label="Деньги")

pyplot.xlabel('Годы')
pyplot.ylabel('Сумма')
pyplot.legend(loc='upper left')
pyplot.show()
