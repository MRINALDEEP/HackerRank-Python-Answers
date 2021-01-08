# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
no_of_shoes = input()
list_of_shoes = input()
list_of_shoes = list_of_shoes.split()
shoe_dict = Counter(list_of_shoes)
shoe_buyer = input()
sold_amount = 0
for i in range(int(shoe_buyer)):
    line = input()
    size,price = line.split()
    if not size in shoe_dict.keys():
        #print('Size '+size+' not available, so no purchase.')
        continue
    else:
        if shoe_dict[size]==0:
            #print('Size '+size+' no longer available, so no purchase.')
            continue
        else:
            shoe_dict[size]-=1
            sold_amount += int(price)
print(sold_amount)

