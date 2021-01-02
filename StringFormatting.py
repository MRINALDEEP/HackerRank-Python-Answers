def print_formatted(number):
    # your code goes here
    width=len(str(bin(number))[2:])
    for i in range(1,number+1):
        deci_val= str(i)
        oct_val=str(oct(i))[2:]
        hex_val=str(hex(i))[2:]
        hex_val=hex_val.upper()
        binary_val=str(bin(i))[2:]
        print(deci_val.rjust(width," ")+" "+oct_val.rjust(width," ")+" "+hex_val.rjust(width," ")+" "+binary_val.rjust(width," "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)