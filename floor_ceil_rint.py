import numpy
numpy.set_printoptions(legacy='1.13')


array_1 = [float(x) for x in input().split()]

array_1= numpy.array(array_1,float)
print(numpy.floor(array_1))
print(numpy.ceil(array_1))
print(numpy.rint(array_1))

