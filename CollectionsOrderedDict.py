# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

dict_of_products = OrderedDict()
no_of_products = int(input())
for i in range(no_of_products):
    temp = input().split()
    temp = temp[::-1]
    price = temp[0]
    product = temp[1:]
    product = " ".join(product[::-1]) 
    
    if product in dict_of_products.keys():
        dict_of_products[product] = dict_of_products[product] + int(price)
    else:
        dict_of_products[product] = int(price)
for k,v in dict_of_products.items():
    print(k+" "+str(v))