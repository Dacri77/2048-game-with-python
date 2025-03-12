def main():
    mainlist=start()
    temp=True
    while temp:
        for i in mainlist:
            print(i)
        direction=input("Enter up, down, left, right!")
        if direction=="up":
            upfunc(mainlist)
        elif direction=="down":
            downfunc(mainlist)
        elif direction=="left":
            leftfunc(mainlist)
        elif direction=="right":
            rightfunc(mainlist)
        temp=zero(mainlist)
        if temp:
            plustwo(mainlist)
    print("GAME OVER!")
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
    return startlist

def upfunc(mainlist):
    banlist=[]
    for i in range(4):
        for j in range(1, 4):
            if mainlist[j][i]!=0:
                for k in range(j-1, -1, -1):
                    if mainlist[k][i]==0:
                        mainlist[k][i]+=mainlist[k+1][i]
                        mainlist[k+1][i]=0
                    elif mainlist[k][i]==mainlist[k+1][i] and [k, i] not in banlist and [k+1, i] not in banlist:
                        mainlist[k][i]+=mainlist[k+1][i]
                        mainlist[k+1][i]=0
                        banlist.append([k, i])

def downfunc(mainlist):
    banlist=[]
    for i in range(4):
        for j in range(2, -1, -1):
            if mainlist[j][i]!=0:
                for k in range(j+1, 4):
                    if mainlist[k][i]==0:
                        mainlist[k][i]+=mainlist[k-1][i]
                        mainlist[k-1][i]=0
                    elif mainlist[k][i]==mainlist[k-1][i] and [k, i] not in banlist and [k-1, i]not in banlist:
                        mainlist[k][i]+=mainlist[k-1][i]
                        mainlist[k-1][i]=0
                        banlist.append([k, i])

def leftfunc(mainlist):
    banlist=[]
    for j in range(4):
        for i in range(1, 4):
            #mainlist[j][i]
            for k in range(i-1, -1, -1):
                if mainlist[j][k]==0:
                    mainlist[j][k]+=mainlist[j][k+1]
                    mainlist[j][k+1]=0
                elif mainlist[j][k]==mainlist[j][k+1] and [j, k] not in banlist and [j, k+1] not in banlist:
                    mainlist[j][k]+=mainlist[j][k+1]
                    mainlist[j][k+1]=0
                    banlist.append([j, k])

def rightfunc(mainlist):
    banlist=[]
    for j in range(4):
        for i in range(2, -1, -1):
            for k in range(i+1, 4):
                if mainlist[j][k]==0:
                    mainlist[j][k]+=mainlist[j][k-1]
                    mainlist[j][k-1]=0
                elif mainlist[j][k]==mainlist[j][k-1] and [j, k] not in banlist and [j, k-1] not in banlist:
                    mainlist[j][k]+=mainlist[j][k-1]
                    mainlist[j][k-1]=0
                    banlist.append([j, k])

def zero(mainlist):
    for i in range(4):
        for j in range(4):
            if mainlist[j][i]==0:
                return True
    return False

def plustwo(mainlist):
    count=0
    for i in range(len(mainlist)):
        for j in range(len(mainlist[i])):
            if mainlist[i][j]==0:
                count+=1
    import random
    temp=random.randint(1, count)
    count=0
    for i in range(len(mainlist)):
        for j in range(len(mainlist)):
            if mainlist[i][j]==0:
                count+=1
                if count==temp:
                    mainlist[i][j]=2
    
main()




