# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:51:31 2020
파이썬 공부하자...
@author: kki9621
"""

import pandas as pd
import statistics
import numpy as np
from scipy.stats import norm
import collections as cln

## bmi지수 구하기---------------------------------------
mydf1 = pd.read_excel('bmi.xlsx', sheet_name = 'bmi')
mydf1.to_excel(r'bmi.xlsx', sheet_name = 'bmi', index = False)

mydfG = mydf1.groupby('gender')
print(mydfG.get_group('M'))

print(mydf1[mydf1['ht']> 175])

print(mydf1.describe())

qidx = mydf1.wt / (mydf1.ht/100) **2
mydf1['bmi'] = qidx
print(mydf1.head())

del mydf1['bmi']
print(mydf1.head())

mydf1.insert(2, 'bmi', qidx)
print(mydf1.head())
## -------------------------------------------------------

x = {i for i in range(1,11)}
print(statistics.median_high(x))

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.array([10,20])
print(y+10)

print(np.arange(3))
print(np.arange(3.0, 7.0))
print(np.arange(3.1, 4.5, 0.5))
print(np.linspace(2.0, 3.0, num = 4))
print(np.linspace(2.0, 3.0, num = 5, retstep = True))

# 행렬--------------------------------------------------

A = np.array([[1,1], [0,1]] )
B = np.array([[2,0], [3,4]] )
 
print(A[0,1])
print(A[0][1])

print(A*B)

print(A @ B)

print(np.ones(5))
print(np.zeros(5))

print(np.ones([5,5]))
myones = np.ones([5,1])
print(myones)

rx = norm.rvs(size = 100)
ave = statistics.mean(rx); stdev = statistics.stdev(rx)
print(ave, stdev)

from scipy.stats import norm
import numpy as np

np.random.seed(100)
print(norm.rvs(size=5))
print(np.random.random(size=5))
print(np.random.choice(10,size=5))


df3 = pd.DataFrame([ [1, 'a', 1.23, True],
                    [4, 'column', 23.5, False],
                    [8, 'with', 45.6, True],
                    [7, 'a', 32.1234, False],
                    [9, 'string', 89.4530, True]],
                   columns=['var0', 'var1', 'var2', 'var3'])

print(df3)

print(df3.iloc[0,2])

def myfcn(me, you):
    mystr = "I am {0}, you are {1}".format(me, you)
    return mystr

print(myfcn("Songyong", "student"))
print(myfcn("student", "Songyong"))
print(myfcn(you="student", me="Songyong"))
print(myfcn(me="Songyong", you="student"))


def myfcn(me, you="unknown"):
    mystr = "I am {0}, you are {1}".format(me, you)
    return mystr

print(myfcn("Songyong", "student"))
print(myfcn("Songyong"))
#print(myfcn(you="student")) # error
print(myfcn(me="Songyong"))

def fcnarg4(arg1, *arg2, **arg3):
  print("arg1 :", arg1)
  print("arg2 :", arg2)
  print("arg3 :", arg3)

fcnarg4(0, 2, 4, 8, t1=1, t2=3, t3=4, name="johnson")


## 파일내의 글자수 세기---------------

f= open('bts.txt', 'r')
lyrics = f.readlines() 
f.close()

allwords = ''

for line in lyrics:
    allwords = allwords + line.strip()
    
counter = allwords.upper().count("DYNAMITE")
print(counter)    

f= open('bts.txt', 'r')
counter = 0
for line in f:
    lcounter = line.lower().count("dynamite") 
    if lcounter > 0: print(line)
    counter = counter + lcounter
f.close()
print (counter)

##----------------------------------------
f= open('bts.txt', 'r')
lyrics = f.readlines() 
f.close()
mywords = ''.join(lyrics)

freq = cln.Counter(mywords.lower().split())
print(freq)

#-----------------------------------------

cc = cln.Counter({'red':4, 'blue':3})
print("cc: ", list(cc.elements()))
dd = cln.Counter(red = 3, blue = 4)
print("dd: ", list(dd.elements()))

#-----------------------------------------
import collections as cln


def dist3D(p, q):
  distance =  (p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2
  return(distance ** 0.5)
  
Point = cln.namedtuple('Point', 'x, y z')

p1 = Point(0,0,0)
p2 = Point(1,1,1)
print(dist3D(p1,p2))


Person = cln.namedtuple('Person', ['name', 'age', 'gender'])
pp1 = Person('심송용', 24, 'F')
print(pp1)
print(" 이름은", pp1.name, " 나이는", pp1.age, " 성별은", pp1.gender)


#-------------------------------------------------------------------
x = []
for i in range(10):
  x.append(i)
print('x: ', x)

y = [i for i in range(10)]
print('y: ', y)


#=========================================

x = []
for i in range(10):
     if i % 2 == 0:
         x.append(i)
print('x: ', x)

y = [i for i in range(10) if i % 2 == 0]
print('y: ', y)

z = [i if i % 2 == 0 else 'odd' for i in range(10)]
print('z: ', z)

#=========================================
x = [i+j for i in range(3) for j in range(4)]
print('x: ', x)

y = [[i*10 + j for i in range(5)]  for j in range(4)]
print('y: ', y)

z = [[i*10 + j if i != j  else 'diag' for i in range(5)]  for j in range(4) ]
print('z: ', z)

z2 = [[i*10 + j  for i in range(5) if i != j ]  for j in range(4) ]
print('z2: ', z2)

#=================================================================

# mapnreduce1.py
from functools import reduce # for reduce

def power2(x): 
    return x ** 2  

def powerk(x,k): 
     return x ** k
 
def myproduct(x,y):  # for reduce
  return x*y

# We square all numbers using map() 
numbers1 = [i for i in range(1,11)]
result = map(power2, numbers1) 
print(list(result)) 

result = map(powerk, numbers1, [4]*10 ) 
print(list(result)) 

numbers2 = [i for i in range(11,21)]
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 

#============================================

result = reduce(myproduct, numbers1)
print(result) 

result = reduce(lambda x, y: x*y, numbers1)
print(result) 
