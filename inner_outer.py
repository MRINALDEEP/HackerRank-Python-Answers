import numpy

array_1 = [int(x) for x in input().split()]
array_2 = [int(x) for x in input().split()]


array_1 = numpy.array(array_1)
array_2 = numpy.array(array_2)


arr_1 = numpy.array(array_1)
arr_2 = numpy.array(array_2)
print(numpy.inner(arr_1,arr_2))
print(numpy.outer(arr_1,arr_2))
