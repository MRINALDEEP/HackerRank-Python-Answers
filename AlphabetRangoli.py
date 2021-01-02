
def create_string(num_of_char,size):
       max_ascii = 96+ size
       temp =[]
       for i in range(num_of_char):
        temp.append(chr(max_ascii - i))
       temp = temp + temp[-2::-1]
       return "-".join(temp) 
def print_rangoli(size):
    if not (0 < size <27):
        print("Contraint Does not match")
        exit()
    line_size = 2*(2*size-1)-1
    for i in range(1,size):
        print(create_string(i,size).center(line_size,"-"))
    for j in range(size,0,-1):
        print(create_string(j,size).center(line_size,"-"))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)