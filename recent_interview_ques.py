
def flatten_list(x: list):
    flat_list = []
    for i in x:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list

l = [1,2,3,[4,5,6,[7,8,9,[10,11,12]]]]
print(flatten_list(l))


l = [1,2,3,4,2,5,6,4] # find the repeated element

def find_repeated_element(l: list):
    for i in set(l):
        if l.count(i) > 1:
            return i
    else:
        return False
    
ele = [i for i in set(l) if l.count(i) > 1]
print(ele)

print(find_repeated_element(l))


def has_duplicate_words(sentence):
    words = sentence.lower().split()  # Convert to lowercase to handle case-insensitive comparison
    return len(words) != len(set(words))

print(has_duplicate_words("This is a test"))               # False
print(has_duplicate_words("This is a test test"))          # True
print(has_duplicate_words("Hello world hello")) 


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Generate matrix transpose by list comprehension to get M = [[1,4,7],[2,5,8],[3,6,9]]
transpose = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
# transpose = [list(row) for row in zip(*M)]
print(transpose)


def find_duplicate_words(sentence):
    words = sentence.lower().split()
    seen = set()
    duplicates = set()
    
    for word in words:
        if word in seen:
            duplicates.add(word)
        else:
            seen.add(word)
    
    return list(duplicates)

sentence = "This is a test and this is only a test"
print(find_duplicate_words(sentence))  # ['this', 'is', 'a', 'test']