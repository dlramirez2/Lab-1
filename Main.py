# Course: CS2302
# @Author: Carlos Montgomery
# @Assignment: Lab 1 Recursion
# Instructor: Diego Aguirre
# Teaching Assistant: Anindita Nath
# Last Modification: 09 / 14 / 18

import hashlib
import string
import itertools


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def main():
    hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    print(hex_dig)


# This reads the "password_file.txt" and stores each aspect of the record to it's own variable
def read_file():
    file_open = open("password_file.txt", "r")
    for line in file_open:
        fields = line.split(",")  # This used to separate and read in between the comas
        # Each field to the record is stored to their own variable
        username = fields[0]
        salt_value = fields[1]
        hash_password = fields[2]
        # print("Username: " + username + "  Salt Value: " + salt_value + "  Password: " + hash_password)
        # this is used to test if each value is correctly stored
        return salt_value


# The following code is used to create every possible combination of digits.
digits = string.digits
def method2(min,max):
    num = itertools.product(digits, repeat=min)
    for prod in itertools.product(num):
        string = ''.join([''.join(k) for k in prod])
        file_open = open("password_file.txt", "r")
        for line in file_open:
            fields = line.split(",")  # This used to separate and read in between the comas
            # Each field to the record is stored to their own variable
            username = fields[0]
            salt_value = fields[1]
            hash_password = fields[2]
            new_password = salt_value+ str(string)
            if (hash_with_sha256(new_password) == hash_password):
                print(new_password + "  "+ hash_password )
            else:
                print(hash_with_sha256(new_password)+ '  =  '+ hash_password)
        if min < max:
            return method2(min+1,max)


method2(3,7)