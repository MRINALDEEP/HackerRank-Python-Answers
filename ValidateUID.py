# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def check_uid(uid):
    length_of_uid = len(uid)
    matching_uid = re.match("^[A-Za-z0-9]+$", uid)
    if matching_uid and  length_of_uid == 10:    
        list_of_digits = re.findall("\d", uid)
        list_of_uppercase = re.findall("[A-Z]", uid)
        list_of_aplhabet = re.findall("[A-Za-z]",uid)
        duplicate_digits = True if len(list_of_digits) != len(set(list_of_digits)) else False
        duplicate_alphabet = True if len(list_of_aplhabet) != len(set(list_of_aplhabet)) else False
        if len(list_of_uppercase) >=2 and len(list_of_digits) >=3 and not duplicate_alphabet and not duplicate_digits:
            print("Valid")
            return 0
    print("Invalid")
test_cases = int(input())
for i in range(test_cases):
    uid = input()
    check_uid(uid)
    