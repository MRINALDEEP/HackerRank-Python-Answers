
for i in range(1,int(input())):
   # print(sum( [10**x for x in range(0,i)])*i)
   print(sum(map(lambda x: 10**x, range(i)))*i)
   