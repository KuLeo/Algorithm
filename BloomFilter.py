import bitarray
import hashlib
import random
import string
import sys
import time


class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = bitarray.bitarray(size)
        self.list = [0] * size
        self.bit_array.setall(False)
        self.hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha224]

    def add_data(self, data):
        for hash_func in self.hash_functions:
            index = int(hash_func(data).hexdigest(), 16) % self.size
            self.bit_array[index] = 1
            self.list[index] = 1

    def is_data_exist(self, data):
        result = bitarray.bitarray([True])
        for hash_func in self.hash_functions:
            index = int(hash_func(data).hexdigest(), 16) % self.size
            result &= self.bit_array[index:index + 1]

        if result[0]:
            return True
        else:
            return False


if __name__ == "__main__":
    bf_size = 20000
    bf_contain_data_size = 1000
    test_case_amount = 1000
    random.seed(time.time())

    b = BloomFilter(bf_size)
    s = set()
    d = {}

    for i in range(bf_contain_data_size):
        input_data = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
        input_data = str.encode(input_data)
        b.add_data(input_data)
        s.add(input_data)
        d[input_data] = 1

    false_positive_amount = 0

    for i in range(test_case_amount):
        input_data = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
        input_data = str.encode(input_data)
        if b.is_data_exist(input_data) ^ (input_data in s):
            false_positive_amount += 1

    fail_rate = round((false_positive_amount / test_case_amount) * 100, 2)
    print("{:20} {}\n".format("success case amount:", test_case_amount - false_positive_amount))
    print("{:20} {}\n".format("fail case amount:", false_positive_amount))
    print("{:20} {}%\n".format("fail rate:", fail_rate))
    print("{:20} {} bytes\n".format("bf bit array size:", sys.getsizeof(b.bit_array.tobytes())))
    print("{:20} {} bytes\n".format("bf list size:", sys.getsizeof(b.list)))
    print("{:20} {} bytes\n".format("set size:", sys.getsizeof(s)))
    print("{:20} {} bytes\n".format("dict size:", sys.getsizeof(d)))
