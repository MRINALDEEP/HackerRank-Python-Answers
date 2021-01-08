# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
no_of_elements = int(input())
elements = input().split()
size = int(input())
temp = [int(i) for i in range(1,no_of_elements+1)]
combinations_list = combinations(temp,size)
indices_of_a = []
for ind,val in enumerate(elements):
    if val == 'a':
        indices_of_a.append(ind+1)
a_comb=0
total_comb=0
for comb in combinations_list:
    total_comb+=1
    for i in indices_of_a:
        if i in comb:
            a_comb+=1
            break

print("{:.4f}".format(a_comb/total_comb))