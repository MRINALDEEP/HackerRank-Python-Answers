# Enter your code here. Read input from STDIN. Print output to STDOUT
doormat_dimension = input()
n, m  = doormat_dimension.split()
try:
    n, m  = int(n), int(m)
except Exception:
    print("Please Enter Integer Values")
    print("Exiting")
    exit()
if not 5 < n < 101 or not 15 < m < 303:
    print("values does not met the contraints")
    exit()
if not m == 3*n:
    print("m : n should be 3. Exiting")
    exit()
if n%2==0:
    print("values should be odd numbers only")
    exit()
design_pattern = ".|."
welcome_sign="WELCOME"  
for i in range(1,n+1):
    if i < ((n+1)//2):
        temp = (2*i - 1)*design_pattern
    elif i > ((n+1)//2):
        temp = (2*(n+1-i) -1)*design_pattern
    elif i==((n+1)//2):
        temp=welcome_sign
    print(temp.center(m,"-"))
    
