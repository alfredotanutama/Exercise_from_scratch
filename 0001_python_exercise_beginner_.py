# -*- coding: utf-8 -*-
"""0001-Python exercise beginner .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZCi_RFnt3ZcfIIq8MSTcHMTDkj13TEOq

From https://www.youtube.com/watch?v=ODjFDZC_TyA&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f&index=5

#1
"""

ctr=0

for i in range(1,10):
  if i % 2 == 0:
    print(i)
    ctr = ctr + 1
print('We have', ctr , 'even numbers')

"""#2"""

for i in range(7):
  print(i)

n=7
for i in range(1,n+1):
  print(i)

n=7
for i in range(1,n+1):
  print(i*'*')