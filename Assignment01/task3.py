# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LW8k2Jnwtw0dsoGgEkXNPftUZ-XPq0GL
"""

from sys import dont_write_bytecode
input_file= open('/content/input3.txt', mode='r')
output_file= open('output3.txt', mode='w') 

dic= {}
node1=2
c=node1-2
c=0
for i in input_file:
    u=2
    c+=u-1
    c+=1
    if c<0:
        pass

    elif 0 < c <2:
        e=0
        node2=i[e-1]
    elif 2 <=c:
        b=0
        item1= i
        item2=item1.split()
        b1=b+1
        if c==0:
            dic[item2]=[]
        dic[item2[b]]=item2[b1::1]


visited=[0]*c
printed=[]

def DFS_VISIT(graph,node):
     visited[int(node)-1]=1
     printed.append(node)
     for node in graph[node]:
         if node not in visited:
             DFS_VISIT(dic, node)

def DFS(graph,endPoint):
    for node in graph:
        if node not in visited:
            DFS_VISIT(dic, '1') 

    for a in printed:
        if a==endPoint:
            break
        else:
            print(a,end=' ')
        
        output_file.write(a+' ')
  


DFS(dic, '12')
input_file.close()
output_file.close()