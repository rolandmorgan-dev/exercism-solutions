def append(list1, list2):
    return list1 + list2

def concat(lists):
    return [num for item in lists for num in item]

def filter(function, list):
    return [num for num in list if function(num)]

def length(list):
    return sum(1 for index in list)

def map(function, list):
    return [function(num) for num in list]

def foldl(function, list, init):
    for el in list:
        init = function(init, el)
    return init

def foldr(function, list, init):
    for el in reversed(list):
        init = function(init, el)
    return init

def reverse(list):
    return list[::-1]
