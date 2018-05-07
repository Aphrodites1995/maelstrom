class monster(object):
    def __init__(self):
        self.name=''
        self.equipment=[]
        self.chargeregen=0
        self.stats=[]
        self.drop=[]
mo1 = monster()
mo1.name='Dire Wolf'
mo1.equipment=['w1','w2','w3','w4','w5','w6','w7']
mo1.chargeregen=3
mo1.stats=[1,1,1,10,10,10]
mo1.drop=['w2']

mo2 = monster()
mo2.name='Bat'
mo2.equipment=['w2','w2','w3','w4','w5','w6','w7']
mo2.chargeregen=3
mo2.stats=[1,1,1,15,15,10]
mo2.drop=['w2','w2']
mo3 = monster()

mo3.name='Witch'
mo3.equipment=['w8','w2','w3','w4','w5','w6','w7']
mo3.chargeregen=3
mo3.stats=[1,1,1,25,25,100]
mo3.drop=['w8']
