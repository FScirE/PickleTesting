import random
import pickle
from tqdm import tqdm
import string



def random_data_generator():

    valid_characters = string.ascii_letters + string.digits
    tough_characters = string.punctuation + ']'
    non_ascii = ''.join(chr(i) for i in range(128, 1114111))

    all_characters = valid_characters + tough_characters + non_ascii

    string1 = "shdajdkhsabndsajhd4628=)....../(&/%&€%#€)"

    test_content = list(random.choices(all_characters, k=100))

    test_bool = False

    while True:
        test_bool = not test_bool
        test_string = ''.join(test_content)
        test_content[random.randint(0,99)] = random.choice(all_characters)
        x = random.randint(1,4)
        if x == 1:
            test_value = test_bool
        elif x == 2:
            test_value = test_string
        elif x == 3:
            test_value = random.randint(-1_000_000_000_000, 1_000_000_000_000)
        else:
            test_value = test_content
        

        string1 = fuzzing_mutator_slow(string1)
        yield {'field_1': string1, #string
               'field_2': '\u005C' + random.choice(all_characters), 
               'field_3': random.randint(-1_000_000_000_000, 1_000_000_000_000), #integer
               'field_4': {test_string: test_value}, #object
               'field_5': test_content, #list
               'field_6': test_bool, #bool
               }  # maybe you have a better idea


def fuzzing_mutator_slow(string):
    """This is a helper function that mutates a given valid input.
    Note that this function does not use a seed, therefore the tests might not be reproducable. """
    str = list(string)
    count=0
    while (count <= 2):
        char_to_mutate=random.randint(0, len(string)-1)

        if ord(str[char_to_mutate])+5>240:
            new_ascii = 0
        else:
            new_ascii=ord(str[char_to_mutate])+ random.randint(0, 15)
        str[char_to_mutate]=chr(new_ascii)
        count+=1
    new_string = ''.join(str)

    return new_string

def main():
    data_generator = random_data_generator()
    exceptions = []
    mismatches = []
    for _ in tqdm(range(1000000)):
        data = next(data_generator)
        try:
            # Serialize and deserialize the data using pickle
            serialized = pickle.dumps(data)
            deserialized = pickle.loads(serialized)
            # Compare original and deserialized data
            if data != deserialized:
                mismatches.append((data, deserialized))
        except Exception as e:
            exceptions.append((e, data))
    
    print(f'{len(exceptions)} exceptions and {len(mismatches)} mismatches found')

if __name__ == '__main__':
    main()
