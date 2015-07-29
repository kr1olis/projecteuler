# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

__author__ = 'krio'
# function, which find all prime number by optimal way

def simple_numbers(num):
    a = []
    for i in range(num+1):
        a.append(i)
    a[1] = 0
    lst = []

    i = 2
    while i <= num:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, num+1, i):
                a[j] = 0
        i += 1
    return lst

# find prime number to 20 or whatever you want
#number=int(input('write your number =')) #you can uncomment this string, and give a chance for user make decision, what number he wants
number=20
lcm = simple_numbers(number)

# compute all of multipliers for each number from 2 to 20, write it in lst
lst = []
for i in range(2,number+1):
    for y in lcm:
        if i%y==0:
            lst.append(y)
            aid=i/y
            if aid == 1:
                break
            else:
                while aid!=1:
                    for x in lcm:
                        if aid%x == 0:
                            lst.append(x)
                            aid=aid/x
                break
list=lst

# find sequence of all pair key:value, and leave only max parameter of value for each key

prev = list[0]
dictio = {}
counter=0
findLastcharacter=0
for x in list:
    findLastcharacter+=1
    if findLastcharacter == len(list):
        if list[-1] == list[-2]:
            counter+=1
            if x in dictio:
                if dictio.get(x)>counter:
                    continue
                else:
                    dictio[x] = counter
            else:
                dictio[x] = counter
        elif list[-1] != list[-2]:
            if prev in dictio:
                if dictio.get(prev)>counter:
                    continue
                else:
                    dictio[prev] = counter
            else:
                dictio[prev] = counter
            counter=1
        if x in dictio:
            if dictio.get(x)>counter:
                continue
            else:
                dictio[x] = counter
        else:
            dictio[x] = counter
    elif x == prev:
        counter+=1
    elif x != prev:
        if prev in dictio:
            if dictio.get(prev)>counter:
                prev = x
                counter = 1
                continue
            else:
                dictio[prev] = counter
        else:
                dictio[prev] = counter
        prev = x
        counter = 1
out = []
for z in dictio.keys():
    out.append(z**dictio.get(z))
result=1
for v in out:
    result*=v
print(result)