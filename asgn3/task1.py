from mylib import *
import string
import random

#Task1 : Exploring Pseudo Randomness and Collision Resistence
'''
#a

print("----------part a -------------")
string1 = "Hello world"
digest1 = modified_sha256(string1)
print(digest1)
print(len(digest1))

digest2 = modified_sha256(string1, 1)
print(digest2)
print(len(digest2))

#b
print("----------part b -------------")
string1 = 'ab'
binary_str = str2bin(string1)
print(f"ab = {binary_str}")

string2 = 'ac'
binary_str2 = str2bin(string2)
print(f"ac = {binary_str2}")

print("Comparing hash digest of `ab` and `ac`")
print(modified_sha256(string1))
print(modified_sha256(string2))
print("\n")
'''
#c

#Hash modified range : 8bit(1byte)
bit_restrict = 16 
check_collide(bit_restrict)
