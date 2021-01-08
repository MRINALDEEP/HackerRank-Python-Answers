# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
no_of_student = input()
cloumns = input()
Student = namedtuple("Student",cloumns)
total_marks=0
for i in range(int(no_of_student)):
    val1,val2,val3,val4 = input().split()
    stu = Student(val1,val2,val3,val4)
    total_marks += int(stu.MARKS)
print("{:.2f}".format(total_marks/int(no_of_student)))        