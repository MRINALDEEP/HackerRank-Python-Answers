# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
no_of_credit_cards = int(input())
for i in range(no_of_credit_cards):
    credit_card_no = input()
    regular_expression_check = re.match("^[4|5|6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$",credit_card_no)
    if regular_expression_check:
        credit_card_no = credit_card_no.replace("-","")
        conse_char_check = re.findall("(.)\\1{3,}",credit_card_no)
        if not conse_char_check:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")