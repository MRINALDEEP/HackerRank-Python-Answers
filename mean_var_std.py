import numpy

x,y = [int(a) for a in input().split()]
array_1 = []
for i in range(x):
    temp = [float(j) for j in input().split()]
    array_1.append(temp)
my_array = numpy.array(array_1,int)
print(numpy.mean(my_array,axis=1))
print(numpy.var(my_array,axis=0))
print(round(numpy.std(my_array,axis=None),11))