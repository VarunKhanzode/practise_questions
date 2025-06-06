
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