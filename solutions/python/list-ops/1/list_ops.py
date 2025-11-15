def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for item in lists:
        result.extend(item)
    return result

def filter(function, list):
    return [num for num in list if function(num) == True]

def length(list):
    return sum(1 for index in list)

def map(function, list):
    return [function(num) for num in list]

def foldl(function, list, initial):
    acc = initial
    for el in list:
        acc = function(acc, el)
    return acc

def foldr(function, list, initial):
    acc = initial
    for el in reversed(list):
        acc = function(acc, el)
    return acc

def reverse(list):
    return [item for item in reversed(list)]
