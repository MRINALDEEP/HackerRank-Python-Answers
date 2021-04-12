import numpy


x,y = [int(a) for a in input().split()]
array_1 = []
for i in range(x):
    temp = [int(j) for j in input().split()]
    array_1.append(temp)

my_array = numpy.array(array_1)
temp_sum = numpy.sum(my_array,axis=0)
result_prod = numpy.prod(temp_sum) 
print(result_prod)