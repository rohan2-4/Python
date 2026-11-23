# Find the frequency of every element in a list.
a = ['python','c','python','java','c','c++']
freq ={}
for word in a:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)