import pickle
import os
import unittest

raw_dct = {
    'pickle_bool': [],
    'pickle_class': [],
    'pickle_complex': [],
    'pickle_dict': [],
    'pickle_float': [],
    'pickle_float_accuracy': [],
    'pickle_func': [],
    'pickle_instance': [],
    'pickle_int': [],
    'pickle_list': [],
    'pickle_string': [],
    'pickle_tuple': [],
    'pickle_nested_structures': [],
    'pickle_unicode': []

}
dct = {
    'pickle_bool': [],
    'pickle_class': [],
    'pickle_complex': [],
    'pickle_dict': [],
    'pickle_float': [],
    'pickle_float_accuracy': [],
    'pickle_func': [],
    'pickle_instance': [],
    'pickle_int': [],
    'pickle_list': [],
    'pickle_string': [],
    'pickle_tuple': [],
    'pickle_nested_structures': [],
    'pickle_unicode': []
}

#test for unicode
def read_desired_pickle(name):
    for i in range(7, 12):
        with open(f'3.{i}/{name}/darwin.pkl', 'rb') as pkl:
            data = pkl.read()
            raw_dct[name].append((data, f'mac3.{i}'))
            dct[name].append((pickle.loads(data), f'mac3.{i}'))
            pkl.close()
        with open(f'3.{i}/{name}/linux.pkl', 'rb') as pkl:
            data = pkl.read()
            raw_dct[name].append((data, f'ubuntu3.{i}'))
            dct[name].append((pickle.loads(data), f'ubuntu3.{i}'))
            pkl.close()
        with open(f'3.{i}/{name}/windows.pkl', 'rb') as pkl:
            data = pkl.read()
            raw_dct[name].append((data, f'windows3.{i}'))
            dct[name].append((pickle.loads(data), f'windows3.{i}'))
            pkl.close()
        

class TestPickleConsistency(unittest.TestCase):
    def test_pickle_bool(self):
        read_desired_pickle('pickle_bool')
        # check raw
        for e in raw_dct['pickle_bool']:
            self.assertEqual(e[0], raw_dct['pickle_bool'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_bool'][0][1])
        # check loaded
        for e in raw_dct['pickle_bool']:
            self.assertEqual(e[0], dct['pickle_bool'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_bool'][0][1])
    
    def test_pickle_class(self):
        read_desired_pickle('pickle_class')
        # check raw
        for e in raw_dct['pickle_class']:
            self.assertEqual(e[0], raw_dct['pickle_class'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_class'][0][1])
        # check loaded
        for e in raw_dct['pickle_class']:
            self.assertEqual(e[0], dct['pickle_class'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_class'][0][1])
    
    def test_pickle_complex(self):
        read_desired_pickle('pickle_complex')
        # check raw
        for e in raw_dct['pickle_complex']:
            self.assertEqual(e[0], raw_dct['pickle_complex'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_complex'][0][1])
        # check loaded
        for e in raw_dct['pickle_complex']:
            self.assertEqual(e[0], dct['pickle_complex'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_complex'][0][1])
    
    def test_dict(self):
        read_desired_pickle('pickle_dict')
        # check raw
        for e in raw_dct['pickle_dict']:
            self.assertEqual(e[0], raw_dct['pickle_dict'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_dict'][0][1])
        # check loaded
        for e in raw_dct['pickle_dict']:
            self.assertEqual(e[0], dct['pickle_dict'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_dict'][0][1])
    
    def test_float(self):
        read_desired_pickle('pickle_float')
        # check raw
        for e in raw_dct['pickle_float']:
            self.assertEqual(e[0], raw_dct['pickle_float'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_float'][0][1])
        # check loaded
        for e in raw_dct['pickle_float']:
            self.assertEqual(e[0], dct['pickle_float'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_float'][0][1])
    
    def test_float_accuracy(self):
        read_desired_pickle('pickle_float_accuracy')
        # check raw
        for e in raw_dct['pickle_float_accuracy']:
            self.assertEqual(e[0], raw_dct['pickle_float_accuracy'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_float_accuracy'][0][1])
        # check loaded
        for e in raw_dct['pickle_float_accuracy']:
            self.assertEqual(e[0], dct['pickle_float_accuracy'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_float_accuracy'][0][1])
    
    def test_func(self):
        read_desired_pickle('pickle_func')
        # check raw
        for e in raw_dct['pickle_func']:
            self.assertEqual(e[0], raw_dct['pickle_func'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_func'][0][1])
        # check loaded
        for e in raw_dct['pickle_func']:
            self.assertEqual(e[0], dct['pickle_func'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_func'][0][1])

    def test_instance(self):
        read_desired_pickle('pickle_instance')
        # check raw
        for e in raw_dct['pickle_instance']:
            self.assertEqual(e[0], raw_dct['pickle_instance'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_instance'][0][1])
        # check loaded
        for e in raw_dct['pickle_instance']:
            self.assertEqual(e[0], dct['pickle_instance'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_instance'][0][1])
    
    def test_int(self):
        read_desired_pickle('pickle_int')
        # check raw
        for e in raw_dct['pickle_int']:
            self.assertEqual(e[0], raw_dct['pickle_int'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_int'][0][1])
        # check loaded
        for e in raw_dct['pickle_int']:
            self.assertEqual(e[0], dct['pickle_int'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_int'][0][1])
    
    def test_list(self):
        read_desired_pickle('pickle_list')
        # check raw
        for e in raw_dct['pickle_list']:
            self.assertEqual(e[0], raw_dct['pickle_list'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_list'][0][1])
        # check loaded
        for e in raw_dct['pickle_list']:
            self.assertEqual(e[0], dct['pickle_list'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_list'][0][1])
    
    def test_string(self):
        read_desired_pickle('pickle_string')
        # check raw
        for e in raw_dct['pickle_string']:
            self.assertEqual(e[0], raw_dct['pickle_string'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_string'][0][1])
        # check loaded
        for e in raw_dct['pickle_string']:
            self.assertEqual(e[0], dct['pickle_string'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_string'][0][1])
    
    def test_tuple(self):
        read_desired_pickle('pickle_tuple')
        # check raw
        for e in raw_dct['pickle_tuple']:
            self.assertEqual(e[0], raw_dct['pickle_tuple'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_tuple'][0][1])
        # check loaded
        for e in raw_dct['pickle_tuple']:
            self.assertEqual(e[0], dct['pickle_tuple'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_tuple'][0][1])

    def test_nested_structures(self):
        read_desired_pickle('pickle_nested_structures')
        # check raw
        for e in raw_dct['pickle_nested_structures']:
            self.assertEqual(e[0], raw_dct['pickle_nested_structures'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + raw_dct['pickle_nested_structures'][0][1])
        # check loaded
        for e in raw_dct['pickle_nested_structures']:
            self.assertEqual(e[0], dct['pickle_nested_structures'][0][0], msg='\nUsing (OS+PythonVer): ' + e[1] + ' compared with ' + dct['pickle_nested_structures'][0][1])

if __name__ == '__main__':
    unittest.main()
