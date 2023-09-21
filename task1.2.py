import math
import os
import random
import re
import sys

s = input(str("Enter the company name "))

print(len(s))

for i in range(len(s)):
    if (s.count(s[i]) == 6):
        print(s[i], "count is 6")
        break
for i in range(len(s)):
    if (s.count(s[i]) == 5):
        print(s[i], "count is 5")
        break
for i in range(len(s)):
    if (s.count(s[i]) == 4):
        print(s[i], "count is 4")
        break
for i in range(len(s)):
    if (s.count(s[i]) == 3):
        print(s[i], "count is 3")
        break
for i in range(len(s)):
    if (s.count(s[i]) == 2):
        print(s[i], "count is 2")
        break


