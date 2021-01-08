# Enter your code here. Read input from STDIN. Print output to STDOUT

A=set(int(i) for i in input().split())
valid = True
no_of_subsets = int(input())
for i in range(no_of_subsets):
    N = set(int(j) for j in input().split())
    is_super_set = A.issuperset(N)
    if not is_super_set:
        valid=False
        break           
print(valid)