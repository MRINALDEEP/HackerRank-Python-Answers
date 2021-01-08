# Enter your code here. Read input from STDIN. Print output to STDOUT


from collections import deque
d = deque()
no_of_command=int(input())
for i in range(no_of_command):
    command = input().split()
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
print(" ".join(d))