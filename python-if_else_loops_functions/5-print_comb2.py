#!/usr/bin/python3
for i in range(99):
    print("{:02d}".format(i), end=', ')
else:
    i += 1
    print("{:02d}".format(i))
