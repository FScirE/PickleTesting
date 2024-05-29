import pickle
import unittest
import string

class test_class():
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
        
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pickle_list = []
pickle_list.append(pickle.dump(0.00000000000003)) #float
pickle_list.append(pickle.dump("!%,'楄香效桴!%,'")) #eric demonic creation
pickle_list.append(pickle.dump(('.','#'))) #tuple
pickle_list.append(pickle.dump(string.punctuation)) #punctuation
pickle_list.append( { 'test!//': 0.0000004333, '//!test': 0.0000004333, '\\\\\\\\nest': { '\\test\n': 20000000 } }) #dictionary (nested)

a = test_class()
b = test_class()
a.x = 1
a.y = 2
b.y = 2
b.x = 1
pickle_list.append(pickle.dump(a)) #class 1
pickle_list.append(pickle.dump(b)) #class 2

pickle_list.append(pickle.dump(fibonacci))
pickle_list.append(pickle.dump(open('main.py')))

test_runner = 'name'
with open(test_runner + '.txt', 'w') as file:
    for p in pickle_list:
        file.write(p + '\n')
    file.close()
