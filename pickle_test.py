import unittest
import pickle
import platform
import os

class class_to_test():
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'class_to_test(x={self.x}, y={self.y})'

    def __eq__(self, other):
        if isinstance(other, class_to_test):
            return self.x == other.x and self.y == other.y
        return False


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def get_os_suffix():
    return platform.system().lower()
    
def get_python_version():
    splitted = platform.python_version().split('.')
    combined = splitted[0] + '.' + splitted[1]
    return combined

class TestPickle(unittest.TestCase):
    def test_pickle_string(self):
        data = 'test/test%&!.,;'
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_string{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))

    def test_pickle_int(self):
        data = 44744
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_int{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))

    def test_pickle_class(self):
        data = class_to_test
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_class{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))
    
    def test_pickle_instance(self):
        data = class_to_test(1, 2)
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_instance{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f: 
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))
    
    def test_pickle_dict(self):
        data = {"a": 1, "b": 2, "c": {"d": 12, "e": 21}}
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_dict{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))

    def test_pickle_list(self):
        data = [1, 2, "test,test/!", 3]
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_list{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))
    
    def test_pickle_bool(self):
        data = True
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_bool{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
    
    def test_pickle_float(self):
        data = 3.21
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_float{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))
        
    def test_pickle_func(self):
        data = fibonacci
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_func{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))

    def test_pickle_float_accuracy(self):
        data = 1 / 597673
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_float_accuracy{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))

    def test_pickle_tuple(self):
        data = (1, 2, 3, 'hihi', 0.12345)
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_tuple{os.sep}{get_os_suffix()}.pkl'
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))
    
    def test_pickle_complex(self):
        data = complex(11, 2)
        pickled_data = pickle.dumps(data)
        file_name = f'{get_python_version()}{os.sep}pickle_complex{os.sep}{get_os_suffix()}.pkl' 
        with open(file_name, 'wb') as f:
            f.write(pickled_data)
        self.assertEqual(data, pickle.loads(pickled_data))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__=='__main__':
    unittest.main()
