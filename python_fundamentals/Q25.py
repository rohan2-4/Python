# Create a set containing duplicate numbers. Print the set and demonstrate that duplicates are automatically removed.
set1={1,2,3,4,5,6,7,8,1,3,4}
print(set1)

# Create a set of five programming languages. Add one language, remove one language, and check whether Python exists.
languages ={'python','java','c','c++','PHP'}
languages.add('ruby')
print(languages)
languages.remove('c')
print(languages)
print('python' in languages)