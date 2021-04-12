import numpy

x,y = [int(a) for a in input().split()]

array_1=[]
array_2=[] 
for i in range(x):
    temp=[int(j) for j in input().split()]
    array_1.append(temp)
for i in range(x):
    temp=[int(j) for j in input().split()]
    array_2.append(temp)

array_1 = numpy.array(array_1,int)
array_2 = numpy.array(array_2,int)

print(array_1 + array_2)
print(array_1 - array_2)
print(array_1 * array_2)
print(array_1 // array_2)
print(array_1 % array_2)
print(array_1 ** array_2)