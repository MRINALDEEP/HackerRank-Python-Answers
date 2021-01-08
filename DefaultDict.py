# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
input_line_1 = input()
group_a_size, group_b_size = input_line_1.split()
frequency_dict = defaultdict(list)
check_list = []
for i in range(int(group_a_size)):
    no = input()
    frequency_dict[no].append(str(i+1))
for j in range(int(group_b_size)):
    no = input()
    check_list.append(no)
    
for no in check_list:
    if no in frequency_dict.keys():
        print(" ".join(frequency_dict[no]))
    else:
        print("-1")
