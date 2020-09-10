import math
def hanoi(total,source,aux,dest):
    if total==1:
        print( total," "+source+"--->"+dest)
        return
    hanoi(total-1,source,dest,aux)
    print(total," "+source+"---"+dest)
    hanoi(total-1,aux,source,dest)

var=int(input('how many disk? '))
hanoi(var,'A','B','C')
print('total move: ',int(math.pow(2,var)-1))
