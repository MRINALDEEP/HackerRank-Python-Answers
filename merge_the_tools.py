def merge_the_tools(word, k):
    # your code goes here
    for i in range(0,len(word),k):
        seen = set()
        temp=[x for x in word[i:i+k] if not (x in seen or seen.add(x))]
        print("".join(temp))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)