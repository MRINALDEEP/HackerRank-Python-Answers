
def minion_game(word):
    # your code goes here
    vowels= "AEIOU"
    s_score,k_score=0,0
    for index,letter in enumerate(word):
        if letter in vowels:
            k_score += (len(word) - index)
        else:
            s_score += (len(word) - index)
    if k_score > s_score:
        print("Kevin", k_score)
    elif k_score < s_score:
        print("Stuart", s_score)
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = input()
    minion_game(s)