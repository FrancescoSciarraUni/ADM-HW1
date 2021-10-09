#Say "Hello, World!" With Python

print "Hello, World!"

#Arithmetic Operators

a = int(raw_input())
b = int(raw_input())
s = a+b
d = a-b
p = a*b
print(s)
print(d)
print(p)

#Python: Division

a = int(raw_input())
b = int(raw_input())

print(a//b)
print(a/b)

#Loops

n = int(raw_input())
for i in range(n):
	print(i*i)
	
#Write a function

def is_leap(year):
    leap = False
    
    if year%4 == 0:
        leap = True
        if year%100 == 0 and year%400 == 0:
            leap = True
        elif year%100 == 0 and year%400 != 0:
            leap = False
        else:
            leap = True
            
    else:
        leap = False
    
    return leap

#Print Function

from __future__ import print_function
n = int(raw_input())
out=""
for i in range(n):
    out+=str(i+1)
print(out)

#List Comprehensions

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

perm = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
out = []
for i in perm:
    sum = 0
    for j in i:
        sum+=j
    if sum != n:
        out.append(i)
print(out)

#Find the Runner-Up Score!

n = int(raw_input())
arr = map(int, raw_input().split())
arr.sort()
second = 0
i = 0
while i < len(arr)-1:
    if arr[i] < arr[i + 1]:
        second = arr[i]
    i+=1
print(second)


#Nested Lists

l = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    l.append([name,score])

flat = [i[1] for i in l]
flat.sort()
set_flat = set(flat)
second_lowest = sorted(set_flat)[1]
out = []
for i in l:
    if i[1] == second_lowest:
        out.append(i[0])
out.sort()
for i in out:
    print(i)
    
#Finding the percentage

n = int(raw_input())
student_marks = {}
for _ in range(n):
    line = raw_input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = raw_input()
sum_scores = 0
for i in student_marks[query_name]:
    sum_scores+=i
avrg_scores = sum_scores/len(student_marks[query_name])
print(format(avrg_scores, '.2f'))

#Lists

N = int(raw_input()) 
out = []
arr_comm = []
for i in range(N):
    cmd = raw_input().split()
    for i in range(1,len(cmd)):
        cmd[i] = int(cmd[i])
    if cmd[0] == 'insert':
        out.insert(cmd[1],cmd[2])
    elif cmd[0] == 'print':
        print(out)
    elif cmd[0] == 'remove':
        out.remove(cmd[1])
    elif cmd[0] == 'append':
        out.append(cmd[1])
    elif cmd[0] == 'sort':
        out.sort()
    elif cmd[0] == 'pop':
        out.pop()
    elif cmd[0] == 'reverse':
        out.reverse()
        
#Tuples

n = int(raw_input())
integer_list = map(int, raw_input().split())
print(hash(tuple(integer_list)))

#sWAP cASE

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

#String Split and Join

def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
    

#Python If-Else

#!/bin/python
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2 == 1:
        print("Weird")
    elif n%2 == 0 and 2<=n<=5:
        print("Not Weird")
    elif n%2 == 0 and 6<=n<=20:
        print("Weird")
    elif n%2 == 0 and n>20:
        print("Not Weird")
        

#What's Your Name?

def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first,last))

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
    
#Mutations

def mutate_string(string, position, character):
    out = string[:position] + character +string[position+1:]
    return out
    
#Find a string

def count_substring(string, sub_string):
    counter = 0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
    return counter

#String Validators

s = raw_input()
alnum = False
alpha = False
digit = False
lower = False
upper = False
for i in s:
    if i.isalnum():
        alnum = True
    if i.isalpha():
        alpha = True
    if i.isdigit():
        digit = True
    if i.islower():
        lower = True
    if i.isupper():
        upper = True
print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)

#Text Alignment

thickness = int(raw_input())
letter = 'H'

for i in range(thickness):
    print((letter * i).rjust(thickness - 1) + letter + (letter * i).ljust(thickness - 1))

for i in range(thickness+1):
    print((letter * thickness).center(thickness * 2) + (letter * thickness).center(thickness * 6))

for i in range(int(thickness/2)+1):
    print((letter*(thickness)*5).rjust(thickness*5+thickness/2))

for i in range(thickness+1):
    print((letter * thickness).center(thickness * 2) + (letter * thickness).center(thickness * 6))

for i in range(thickness-1,-1,-1):
    print((letter * i).rjust(thickness*5 - 1) + letter + (letter * i).ljust(thickness*5 - 1))
    
#Text Wrap

def wrap(string, max_width):
    out = ""
    for i in range(0,len(string),max_width):
        out += string[i:i+max_width] + "\n"
    return out

#Capitalize!

def solve(s):
    import string
    return string.capwords(s,sep=" ")
    
#Introduction to Sets

def average(array):
    set_l = set(array)
    sum=0
    for i in set_l:
        sum+=i
    return sum/len(set_l)
    
    
#Symmetric Difference

if __name__ == '__main__':
    import sys
    s = sys.stdin.read()
    
    input_list = s.split('\n')
    
    m = input_list[0]
    set_m = set([int(x)for x in input_list[1].split(" ")])
    
    n = input_list[2]
    set_n = set([int(x)for x in input_list[3].split(" ")])
    
    intersec = set_m.intersection(set_n)
    diff = set_n.difference(intersec).union(set_m.difference(intersec))
    diff = (sorted(diff))
    print("\n".join(map(str, diff)))
    
#No Idea!

if __name__ == '__main__':
    import sys
    s = sys.stdin.read()    
    input_list = s.split('\n')
    
    n,m = input_list[0].split(" ")[0],input_list[0].split(" ")[1]
    int_array = map(int,input_list[1].split(" "))
    set_a = set(map(int,input_list[2].split(" ")))
    set_b = set(map(int,input_list[3].split(" ")))
    
    happiness = 0
    for i in int_array:
        if i in set_a:
            happiness += 1
        elif i in set_b:
            happiness -= 1
            
    print(happiness)

#Set .add()

if __name__ == '__main__':
    n = int(raw_input())
    stamp_set = set()
    for i in range(n):
        stamp_set.add(raw_input())
    print(len(stamp_set))

#Set .discard(), .remove() & .pop()

if __name__ == '__main__':
    from pip._vendor.distlib.compat import raw_input
    raw_input()
    elem_set = set(map(int,raw_input().split(" ")))
    n_command = int(raw_input())
    out_set = set()
    for i in range(n_command):
        cmd = raw_input().split()
        if len(cmd) > 1:
            e = int(cmd[1])
        if cmd[0] == "pop":
            elem_set.pop()
        elif cmd[0] == "remove":
            elem_set.remove(e)
        elif cmd[0] == "discard":
            elem_set.discard(e)
    print(sum(elem_set))

#Set .union() Operation
if __name__ == '__main__':
    n_eng = input()
    eng_std = set(map(int,input().split()))
    b_french = input()
    french_std= set(map(int,input().split()))
    print(len(french_std.union(eng_std.union(eng_std.intersection(french_std)))))

#Set .intersection() Operation

if __name__ == '__main__':
    n_eng = input()
    eng_std = set(map(int,input().split()))
    b_french = input()
    french_std= set(map(int,input().split()))
    print(len(eng_std.intersection(french_std)))
    
#Set .difference() Operation

if __name__ == '__main__':
    n_eng = input()
    eng_std = set(map(int,input().split()))
    b_french = input()
    french_std= set(map(int,input().split()))
    print(len(eng_std.difference(french_std)))

#Set .symmetric_difference() Operation

if __name__ == '__main__':
    n_eng = input()
    eng_std = set(map(int,input().split()))
    b_french = input()
    french_std= set(map(int,input().split()))
    print(len(eng_std.symmetric_difference(french_std)))

#Set Mutations

if __name__ == '__main__':
    from pip._vendor.distlib.compat import raw_input
    raw_input()
    elem_set = set(map(int, raw_input().split(" ")))
    n_command = int(raw_input())
    for i in range(n_command):
        cmd = raw_input().split()[0]
        sup_set = set(map(int, raw_input().split(" ")))
        if (cmd == "intersection_update"):
            elem_set.intersection_update(sup_set)
        elif (cmd == "update"):
            elem_set.update(sup_set)
        elif (cmd == "symmetric_difference_update"):
            elem_set.symmetric_difference_update(sup_set)
        elif (cmd == "difference_update"):
            elem_set.difference_update(sup_set)
    print(sum(elem_set))

#The Captain's Room

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    k = int(raw_input())
    elems = list(map(int, raw_input().split(" ")))
    supp1 = set()
    supp2 = set()
    for i in elems:
        if i not in supp1:
            supp1.add(i)
            supp2.add(i)
        else:
            if i in supp2:
                supp2.remove(i)
    print(supp2.pop())
    
#Check Subset
from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        raw_input()
        set_a = set(map(int, raw_input().split(" ")))
        raw_input()
        set_b = set(map(int, raw_input().split(" ")))
        print(set_a.issubset(set_b))
        
#Check Strict Superset

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    out =[]
    elem_set = set(map(int, raw_input().split(" ")))
    n = int(raw_input())
    for i in range(n):
        s = set(map(int, raw_input().split(" ")))
        out.append(elem_set.issuperset(s))
    print(all(out))

#collections.Counter()

from pip._vendor.distlib.compat import raw_input
from collections import Counter

if __name__ == '__main__':
    x = int(raw_input())
    shoes = map(int, raw_input().split(" "))
    shoes = Counter(shoes)
    n_cust = int(raw_input())
    income = 0
    for i in range(n_cust):
        customer = raw_input().split()
        size = int(customer[0])
        price = int(customer[1])
        if size in shoes.keys() and shoes[size] > 0:
            income += price
            shoes[size] -= 1

    print(income)
    
#DefaultDict Tutorial

from pip._vendor.distlib.compat import raw_input
from collections import Counter
from collections import defaultdict

if __name__ == '__main__':
    words = list(map(int,raw_input().split(" ")))
    n = words[0]
    m = words[1]
    d = defaultdict(list)
    letters = []
    for i in range(n):
        letter = raw_input()
        d[letter].append(i+1)
    for i in range(m):
        letters.append(raw_input())
    for letter in letters:
        if letter in d.keys():
            print(*d[letter])
        else:
            print(-1)

#Collections.namedtuple()

from pip._vendor.distlib.compat import raw_input
from collections import namedtuple

if __name__ == '__main__':
    n = int(raw_input())
    fields = raw_input()
    supp = []
        #.split()
    student = namedtuple('student', fields)
    for i in range(n):
        entry = raw_input().split()
        s = student(*entry)
        supp.append(s)
    sum = 0
    for i in supp:
        sum+=int(i.MARKS)
    print(format(sum/len(supp),".2f"))

#Collections.OrderedDict()

if __name__ == '__main__':
    from collections import OrderedDict
    from pip._vendor.distlib.compat import raw_input
    n = int(raw_input())
    o = OrderedDict()
    for i in range(n):
        row = list(raw_input().split())
        if len(row) > 2:
            item = "{} {}".format(row[0],row[1])
            price = int(row[2])
        else:
            item = row[0]
            price = int(row[1])
        if item in o.keys():
            o[item] += price
        else:
            o[item] = price

    for k,v in o.items():
        print(k,v)

#Word Order

if __name__ == '__main__':
    from collections import OrderedDict
    from pip._vendor.distlib.compat import raw_input

    n = int(raw_input())
    o = {}
    count = 0
    for i in range(n):
        row = raw_input()
        if row in o.keys():
            o[row] += count+1
        else:
            o[row] = count+1
    print(len(o.keys()))
    print(*o.values())

#Collections.deque()

if __name__ == '__main__':
    from collections import deque
    from pip._vendor.distlib.compat import raw_input
    d = deque()
    n = int(raw_input())
    count = 0
    for i in range(n):
        row = raw_input().split()
        cmd = row[0]
        if len(row) > 1:
            value = row[1]
        if cmd == "append":
            d.append(value)
        elif cmd == "appendleft":
            d.appendleft(value)
        elif cmd == "pop":
            d.pop()
        elif cmd == "popleft":
            d.popleft()
    print(*d)

#Company Logo

#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    from collections import Counter
    s = input()
    letters = sorted(s)
    count = Counter(letters)
    for l,c in count.most_common(3):
        print(l,c)

#Calendar Module

if __name__ == '__main__':
    from pip._vendor.distlib.compat import raw_input
    import calendar
    day = list(map(int,raw_input().split()))
    print(calendar.day_name[calendar.weekday(day[2],day[0],day[1])].upper())

#Time Delta

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    format_t = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1,format_t)
    t2 = datetime.strptime(t2, format_t)   
    return str(int(abs(t1-t2).total_seconds()))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
    
#Exceptions

if __name__ == '__main__':
    from pip._vendor.distlib.compat import raw_input
    t = int(raw_input())
    for i in range(t):
        try:
            division = list(raw_input().split())
            print(int(division[0])//int(division[1]))
        except Exception as e:
            print("Error Code: {}".format(e))

#Zipped!

if __name__ == '__main__':
    from pip._vendor.distlib.compat import raw_input
    n_students,n_subject = map(int,raw_input().split())
    avrg = 0
    supp = []
    for i in range(n_subject):
        supp.append(list(map(float,raw_input().split())))
    zppd = zip(*supp)
    for i in zppd:
        for j in i:
            avrg+=j
        print(format(avrg/len(i),".2f"))
        avrg = 0

#Athlete Sort

#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr.sort(key=lambda x:x[k])
    for i in arr:
        print(*i)

#ginortS

if __name__ == '__main__':
    from pip._vendor.distlib.compat import raw_input
    s = raw_input()
    letters_lower = ""
    letters_upper = ""
    numbers_odd = ""
    numbers_even = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                letters_upper+=i
            else:
                letters_lower+=i
        elif i.isdigit():
            if int(i)%2 == 0:
                numbers_even+=i
            else:
                numbers_odd+=i
    letters_lower = "".join(sorted(letters_lower))
    letters_upper = "".join(sorted(letters_upper))
    numbers_odd = "".join(sorted(numbers_odd))
    numbers_even = "".join(sorted(numbers_even))
    print(letters_lower+letters_upper+numbers_odd+numbers_even)

#Map and Lambda Function

cube = lambda x: x**3 

def fibonacci(n):
    i = 0
    n1,n2 = 0,1
    out = []
    while i < n:
        out.append(n1)
        fibo = n1+n2
        n1 = n2
        n2 = fibo
        i+=1
    return out
    
#Detect Floating Point Number

if __name__ == '__main__':
    from pip._vendor.distlib.compat import raw_input
    import re
    t = int(raw_input())

    for i in range(t):
        s = raw_input()
        #print(s)
        if re.match("^[-+]?[0-9]*\.[0-9]+$",s):
            print("True")
        else:
            print("False")

#Re.split()

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Group(), Groups() & Groupdict()

if __name__ == '__main__':
    from pip._vendor.distlib.compat import raw_input
    import re
    #\b([a-zA-Z0-9])\\1\\1+\\b
    #([a-z]{2})|([A-Z]{2})|(\d{2})

    m = re.search(r'([a-zA-Z0-9])\1',raw_input())
    if m:
        print(m.groups()[0])
    else:
        print(-1)

#Birthday Cake Candles

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    max = candles[0]
    count = 0
    for i in candles:
        if i>max:
            max = i
            count = 1
        elif i == max:
            count +=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1 < v2:
        return "NO"
    elif v1 == v2:
        return "NO"
    else:
        while x1 != x2 and x2 > x1:
            x1+=v1
            x2+=v2
        if x1 == x2:
            return "YES"
        else:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising

#!/bin/python3
import math
import os
import random
import re
import sys

def viralAdvertising(n):
    recipients = 5
    cumulative = 0
    for i in range(n):
        liked = math.floor(recipients / 2)
        recipients = liked * 3
        cumulative += liked
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
 
#Recursive Digit Sum

#!/bin/python3
import math
import os
import random
import re
import sys

def rec(n):
    if len(str(n)) == 1:
        return n
    else:
        out = 0
        fullword = str(n)
        out = sum([int(i)for i in fullword])
        return rec(str(out))

def superDigit(n, k):
    first = rec(int(n)*k)
    return rec(first)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr): 
    current_max = arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i] > current_max:
            arr[i+1] = arr[i]
            if i == 0:
                print(*arr)
                arr[i] = current_max
        elif arr[i] < current_max:
            arr[i+1] = current_max
            print(*arr)
            break
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#Insertion Sort - Part 2

#!/bin/python3
import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

#Re.findall() & Re.finditer()

from pip._vendor.distlib.compat import raw_input
import re
s = raw_input()
matches = re.findall(r"[^aiueo]([aiueoAIUEO]{2,})(?=[^aiueo])",s)
if len(matches) > 0:
    for i in matches:
        print(i)
else:
    print(-1)

#Re.start() & Re.end()

from pip._vendor.distlib.compat import raw_input
import re

s = raw_input()
sub = raw_input()
to_find = re.compile(sub)
match = to_find.search(s)
if match is None:
    print("(-1, -1)")
while match:
    print("({}, {})".format(match.start(), match.end()-1))
    match = to_find.search(s, match.start() + 1)

#Regex Substitution

from pip._vendor.distlib.compat import raw_input
import re


def check_sub(li):
    match = (li.group(0))
    if match == "&&":
        return "and"
    elif match == "||":
        return "or"
    
n = int(raw_input())
for i in range(n):
    l = raw_input()
    l = re.sub(r"(?<= )(&&|\|\|)(?= )",lambda x: check_sub(x),l)
    print(l)

#Validating Roman Numerals

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Validating phone numbers

from pip._vendor.distlib.compat import raw_input
import re

n = int(raw_input())
pattern = "^(7|8|9)[0-9]{9}$"
for i in range(n):
    phone = raw_input()
    match = re.match(pattern,phone)
    if match:
        print("YES")
    else:
        print("NO")

#Validating and Parsing Email Addresses

from pip._vendor.distlib.compat import raw_input
import re

n = int(raw_input())
for i in range(n):
    name,address = list(raw_input().split())
    match = re.fullmatch(r'(\b[A-Za-z][A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{1,3}\b)',address[1:-1])
    if match:
        print(name,address)

#Hex Color Code

from pip._vendor.distlib.compat import raw_input
import re

n = int(raw_input())
for i in range(n):
    line = raw_input()
    words = line.split()
    if len(words) > 1 and '{' not in words:
        match = re.findall(r"#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}", line)
        [print(j) for j in match]

#HTML Parser - Part 1

from html.parser import HTMLParser
from pip._vendor.distlib.compat import raw_input
import re


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for l in attrs:
            print('->',l[0],'>',l[1])
    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for l in attrs:
            print('->',l[0],'>',l[1])

parser = MyHTMLParser()
n = int(raw_input())
for i in range(n):
    parser.feed(raw_input())


#HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        lines = data.split("\n")
        if len(lines)>1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    def handle_data(self, data):
        if not data == "\n":
            print(">>> Data")
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values

from pip._vendor.distlib.compat import raw_input
from html.parser import HTMLParser

class MyHTMLParser3(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for l in attrs:
            print('->', l[0], '>', l[1])

    #def handle_endtag(self, tag):
    #    print(tag)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for l in attrs:
            print('->', l[0], '>', l[1])

parser = MyHTMLParser3()

html = ""
n = int(raw_input())
for i in range(n):
    parser.feed(raw_input())


#Validating UID

from pip._vendor.distlib.compat import raw_input
import re
n = int(raw_input())
for i in range(n):
    uid = raw_input().strip()
    if uid.isalnum() and len(uid) == 10:
        if re.search(r"(.*[A-Z]){2,}",uid) and re.search(r"(.*[0-9]){3,}",uid):
            if re.search(r".*(.).*\1+.*",uid):
                print("Invalid")
            else:
                print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")


#XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    count = 0
    if len(node) == 0:
        count += len(node.attrib)
        return count
    else:
        count += len(node.attrib)
        for i in node:
            count += get_attr_number(i)
        return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
    
#XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = -1
def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1

    for child in elem:
        depth(child,level+1)
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
    
#Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        out = []
        for i in l:
            out.append("+91 "+i[-10:-5] + " " + i[-5:])
        f(out)
    return fun

#Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        out = []
        for i in sorted(people,key = lambda x: int(x[2])):
            if i[3] == 'M':
                out.append("Mr. " + i[0]+ " " +i[1])
            else:
                out.append("Ms. " + i[0]+ " " + i[1])
        return out
    return inner

#Arrays

def arrays(arr):
    a = numpy.array(arr,float)
    return numpy.flip(a)

#Shape and Reshape
import numpy

l = list(map(int,input().split()))
print(numpy.reshape(l,(3,3)))

#Transpose and Flatten
import numpy
from pip._vendor.distlib.compat import raw_input
nm = raw_input().split()
n = int(nm[0])
m = int(nm[1])
s = []
for i in range(n):
    s.append(list(map(int,raw_input().split())))
a = numpy.array(s)
print(numpy.transpose(a))
print(a.flatten())


#Concatenate
import numpy
n,m,p = map(int,input().split())
l_n = []
l_p = []
for i in range(n):
    l_n.append(list(map(int,input().split())))
for i in range(m):
    l_p.append(list(map(int,input().split())))
    
a_n = numpy.array(l_n)
a_p = numpy.array(l_p)

print(numpy.concatenate((a_n,a_p),axis=0))

#Zeros and Ones

import numpy

l = list(map(int,input().split()))
print(numpy.zeros(l,int))
print(numpy.ones(l,int))

#Eye and Identity
import numpy

numpy.set_printoptions(legacy='1.13')
n,m = map(int,input().split())
if n == m:
    print(numpy.identity(n))
else:
    print(numpy.eye(n,m))


#Array Mathematics

import numpy


n,m = map(int,input().split())
l1 = []
l2 = []
for i in range(n):
    l1.append(list(map(int,input().split())))
for i in range(n):
    l2.append(list(map(int,input().split())))
a1 = numpy.array(l1)
a2 = numpy.array(l2)
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1//a2)
print(a1%a2)
print(a1**a2)


#Floor, Ceil and Rint

import numpy
numpy.set_printoptions(legacy='1.13')
a = numpy.array(list(map(float,input().split())))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

#Sum and Prod

import numpy
numpy.set_printoptions(legacy='1.13')


n,m = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
a = numpy.array(l)
s = numpy.sum(a,axis=0)
print(numpy.prod(s))

#Min and Max

import numpy
numpy.set_printoptions(legacy='1.13')

n,m = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
a = numpy.array(l)
print(numpy.max(numpy.min(a,axis = 1)))

#Mean, Var, and Std

import numpy

n,m = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
a = numpy.array(l)
print(numpy.mean(a,axis=1))
print(numpy.var(a, axis=0))
numpy.around(a,decimals=11)
a = numpy.std(a,axis = None)
print(numpy.around(a,decimals=11))

#Dot and Cross

import numpy

numpy.set_printoptions(legacy='1.13')
n= int(input())
l1 = []
l2 = []
for i in range(n):
    l1.append(list(map(int,input().split())))
for i in range(n):
    l2.append(list(map(int,input().split())))
a1 = numpy.array(l1)
a2 = numpy.array(l2)
print(numpy.dot(a1,a2))

#Inner and Outer

import numpy

a1 = numpy.array(list(map(int,input().split())))
a2 = numpy.array(list(map(int,input().split())))
print(numpy.inner(a1,a2))
print(numpy.outer(a1, a2))

#Polynomials

import numpy

coefficients = list(map(float,input().split()))
x = int(input())
print(numpy.polyval(coefficients,x))

#Linear Algebra

import numpy
numpy.set_printoptions(legacy='1.13')
n= int(input())
l1 = []
#l2 = []
for i in range(n):
    l1.append(list(map(float,input().split())))

a = numpy.array(l1)
print(numpy.linalg.det(a))
