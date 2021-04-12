import numpy


x,y = [int(a) for a in input().split()]
array_1 = []
for i in range(x):
    temp = [int(j) for j in input().split()]
    array_1.append(temp)
my_array = numpy.array(array_1)

temp_min= numpy.min(my_array,axis=1)
result_max= numpy.max(temp_min)
print(result_max)



