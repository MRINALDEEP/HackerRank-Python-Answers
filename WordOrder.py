# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
no_of_inputs = int(input())
word_freq_dict = OrderedDict()
for i in range(no_of_inputs):
    word = input()
    if word in word_freq_dict.keys():
        word_freq_dict[word]+=1
    else:
        word_freq_dict[word] = 1
print(len(word_freq_dict.keys()))
string_freq=[str(x) for x in word_freq_dict.values()]
print(" ".join(string_freq))
