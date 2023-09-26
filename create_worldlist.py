# TODO : create function for md5
# TODO : create function for sha256
# TODO : implement sha256

import hashlib

file1 = open('wordlist/wordlist.txt', 'r')
Lines = file1.readlines()
file2 = open('wordlist/md5.txt', 'w')

for i in Lines:
    md5hash = hashlib.md5(i.rstrip().encode())
    print(i.rstrip())
    print(md5hash.hexdigest())
#    file2.write(i)
    file2.write(md5hash.hexdigest())
    file2.write("\n")
file2.close()