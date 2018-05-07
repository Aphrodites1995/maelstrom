import random
def chanceword(outof,**kwargs):
    roll=random.randint(0,outof-1)
    reply=0
    before=0
    for key in kwargs:
        if roll<=kwargs[key]+before and before<=roll: # before<=roll<=kwargs[key]+before
            reply=key
        before=before+kwargs[key]
    return reply
            #chanceword(100,none=20,a=60,b=20), 20 percent of none, 60 percert of a, 20 percent of b
def chance(outof,*args):
    roll=random.randint(0,outof-1)
    reply=0
    before=0
    listofchances=[]
    for i in range(0,len(args),1):
        if i%2==0:
            listofchances.append(args[i])
    for j in range(0,len(listofchances),1):
        if roll<=listofchances[j]+before and before<=roll:
            reply=args[2*j+1]
        before=before+listofchances[j]
    return reply
    #syntax: chance(100,20,'a',40,'b',40,3) : 20 percent of a, 40 percent of b, 40 percent of 3
