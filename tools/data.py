import numpy as np
import math
import os
from math import *
import sys

def pssm_g(name,path):

    name+='.pssm'
    f=open(os.path.join(path,name),'r')
    
    rows = f.readlines()
    maxn=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    minn=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ans=[ [0] *20 for i in range(3,len(rows)-6)]
    for i in range(2,22):
        t=[]
        for j in range(3,len(rows)-6):
            t.append(float(rows[j].split()[i]))
        maxn[i-2] = max(t)
        minn[i-2] = min(t)

    for i in range(3,len(rows)-6):
        for j in range(2,22):
            #print(float(rows[i].split()[j])-minn[j-2],maxn[j-2]-minn[j-2])
            ans[i-3][j-2] = (float(rows[i].split()[j])-minn[j-2]) / (maxn[j-2]-minn[j-2])        
    return(ans)


def hhm_g(name,path):
    name+='.hhm'
    f=open(os.path.join(path,name),'r')
    rows = f.readlines()
    maxn=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    minn=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    for i in range(0,len(rows)):
        l = rows[i].split()
        if len(l) == 0:continue
        if l[0] == '#': 
            flag = i
            break

    tmp = []

    for i in range(flag+5, len(rows)-3):
        l = rows[i].split()
        if len(l) == 0:continue
        if l[0].isalpha():
            tmp.append(l[2:-1])

    for i in range(len(tmp)):
        for j in range(20):
            if tmp[i][j] == '*': tmp[i][j] = '10000'
    
    for i in range(20):
        t=[]
        for j in range(len(tmp)):
            t.append(float(tmp[j][i]))
        maxn[i]= max(t)
        minn[i]= min(t)

    
    for i in range(len(tmp)):
        for j in range(20):
            up = float(float(tmp[i][j]) - minn[j])
            down = maxn[j]-minn[j]
            tmp[i][j] = up/down     
    return(tmp)


def spd_g(name,path):
    name+='.spd33'
    f=open(os.path.join(path,name),'r')
    rows = f.readlines()
    maxn=[194.1,30.4,32.3,1,1,1,0.99999,1,0.0209,1,1,1,1,1]
    minn=[0.1,0.5,4.8,0,0,0,-0.999,-1,-0.87546,-1,-1,-0.99999,0.482,-1]
    tmp = []
    for i in range(1,len(rows)):
        l = rows[i].split()[3:]
        tmp.append(l)

    ans = []
    
    for i in range(len(tmp)):
        t=[]
        t.append(float(tmp[i][0]))
        t.append(cos(float(tmp[i][1])))
        t.append(cos(float(tmp[i][2])))
        t.append(cos(float(tmp[i][3])))
        t.append(cos(float(tmp[i][4])))
        t.append(sin(float(tmp[i][1])))
        t.append(sin(float(tmp[i][2])))
        t.append(sin(float(tmp[i][3])))
        t.append(sin(float(tmp[i][4])))
        t.append(float(tmp[i][5]))
        t.append(float(tmp[i][6]))
        t.append(float(tmp[i][7]))
        t.append(float(tmp[i][8]))
        t.append(float(tmp[i][9]))
        ans.append(t)
   
    for i in range(14):
        t=[]
        for j in range(len(ans)):
            t.append(float(ans[j][i]))
        maxn[i] = max(t)
        minn[i] = min(t)
    
    for i in range(len(ans)):
        for j in range(14):
            up = float(float(ans[i][j]) - minn[j])
            down = maxn[j]-minn[j]
            ans[i][j] = up/down    
    return(ans)
        
name=sys.argv[1]
pssm=pssm_g(name,'./feature/')
hhm=hhm_g(name,'./feature/')
spd33=spd_g(name,'./feature/')

f=[]
for i in range(0,len(pssm)):
    f.append(spd33[i]+hhm[i]+pssm[i])

f = np.array(f)
f = np.transpose(f)

np.save('./npdata/'+name+'.npy',f)













