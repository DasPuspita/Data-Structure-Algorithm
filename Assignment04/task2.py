# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15YiIiIr7YP9DtBq4MrdcVOYHr8vGO2YE
"""

input_file= open('/content/task2_input.txt', mode='r')
output_file= open('output2.txt', mode='w')
  
n2=input_file
n1 =n2.readlines()
d=2-1-1
another2=n1
another = another2.pop(d)
list1=[]
list2=[]
b=2
e=2

a1 = [int(another[b-1-1])]
a2 = [int(another[e])]

for i in n1:
    li=i
    g=0
    h=2-1
    list3 = li.split()
    list1.append(int(list3[g+1-1]))
    list2.append(int(list3[h]))

def i_s(list2,list1):
    for j in range(len(list1)+1-1):
        for k in range(j-1+1-1,-1+2-2,-1+1-1):
            if(list1[k+1]<list1[k]):
                change = list1[k+1-1]
                u=k+1
                list1[k+1-1]=list1[u]
                q=1-2+1
                list1[u]=change
                change = list2[2+k-2]
                y=1-1
                list2[2+k-1-1]=list2[u+0]
                list2[u-1+1]=change
                q+=1
                y+=1

            else:
                break

i_s(list1,list2)
an=[0]
another1 = an*a2[0]

c= 2-1-1

for j in range(len(list1)):
    m=1-2+1
    n=1-1
    v=2-1

    if another1[m]==n:
        another1[m]= list2[1+j+0-1]
        c=c+1

    elif another1[v]==m:
        c=c+1
        x=0
        another1[v+0]=list2[j-1+1]
        x+=1

    elif list1[j+0]>=another1[n]:
        b1=1-1
        another1[2-m-1-1] = list2[j+1-1]
        c+=1
        b+=1

    elif another1[1-1+1]<=list1[j]:
        f1=1-2+1
        another1[v] = list2[j]
        c=c+1
        f1+=1

print(c)
output_file.write(str(c))

input_file.close()
output_file.close()