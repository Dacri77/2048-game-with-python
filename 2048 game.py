def main():
    mainlist=start()
    direction=input("Enter up, down, left, right!")
    if direction=="up":
        upfunc(mainlist)
    elif direction=="down":
        downfunc(mainlist)
    elif direction=="left":
        leftfunc(mainlist)
    elif direction=="right":
        rightfunc(mainlist)

import random
def start():
    startlist=[[0 for i in range(4)]for j in range(4)]
    e1i1=random.randint(0, 3)
    e1i2=random.randint(0, 3)
    e2i1=random.randint(0, 3)
    e2i2=random.randint(0, 3)
    while e1i1==e2i1 and e1i2==e2i2:
        e1i1=random.randint(0, 3)
        e2i2=random.randint(0, 3)
    startlist[e1i1][e1i2]=2
    startlist[e2i1][e2i2]=2
    print("The game has been started!")
    for i in startlist:
        print(i)
    return startlist

def upfunc(mainlist):
    for i in range(4):
        for j in range(1, 4):
            if mainlist[j][i]!=0:
                for k in range(j-1, -1, -1):
                    if mainlist[k][i]==0 or mainlist[k][i]==mainlist[k+1][i]:
                        mainlist[k][i]+=mainlist[k+1][i]
                        mainlist[k+1][i]=0
    for i in mainlist:
        print(i)

def downfunc(mainlist):
    for i in range(4):
        for j in range(2, -1, -1):
            if mainlist[j][i]:
                for k in range(j+1, 4):
                    if mainlist[k][i]==0 or mainlist[k][i]==mainlist[k-1][i]:
                        mainlist[k][i]+=mainlist[k-1][i]
                        mainlist[k-1][i]=0
    for i in mainlist:
        print(i)

def leftfunc(mainlist):
    for j in range(4):
        for i in range(1, 4):
            #mainlist[j][i]
            for k in range(i-1, -1, -1):
                if mainlist[j][k]==0 or mainlist[j][k+1]==mainlist[j][k]:
                    mainlist[j][k]+=mainlist[j][k+1]
                    mainlist[j][k+1]=0
    for i in mainlist:
        print(i)

def rightfunc(mainlist):
    for j in range(4):
        for i in range(2, -1, -1):
            for k in range(i+1, 4):
                if mainlist[j][k]==0 or mainlist[j][k-1]==mainlist[j][k]:
                    mainlist[j][k]+=mainlist[j][k-1]
                    mainlist[j][k-1]=0
    for i in mainlist:
        print(i)

main()