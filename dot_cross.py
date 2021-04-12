import numpy


no = int (input())

array_1=[]
array_2=[] 
for i in range(no):
    temp=[int(j) for j in input().split()]
    array_1.append(temp)
for i in range(no):
    temp=[int(j) for j in input().split()]
    array_2.append(temp)

array_1 = numpy.array(array_1,int)
array_2 = numpy.array(array_2,int)

print(numpy.dot(array_1,array_2))