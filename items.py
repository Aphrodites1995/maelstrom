import classes
class item(object):
    def __init__(self):
        self.name=''
        self.type=''
        self.dexpen=0
        self.moves=[]
        self.chargeturn=0
        self.addchargeneed=0
        #addchargeturn is how may charge needed to 
        self.equipplace=0
        self.defencechance=0
        #out of 100
        self.defamount=0
w1 = item()
w1.name='hands'
w1.type='body part'
w1.dexpen=0.01
w1.moves=[1,2,3]
w1.chargeturn=7
w1.addchargeneed=2
w1.equipplace=[0,1]
w1.defencechance=0
w1.defamount=0

w2 = item()
w2.name='sharp claw'
w2.type='claw'
w2.dexpen=0.02
w2.moves=[4,5,6,7]
w2.chargeturn=10
w2.addchargeneed=2
w2.equipplace=[0,1]
w2.defencechance=3
w2.defamount=1

w3 = item()
w3.name='body helmet'
w3.type='body armor'
w3.dexpen=0.01
w3.moves=[]
w3.chargeturn=0
w3.addchargeneed=0
w3.equipplace=[2]
w3.defencechance=1
w3.defamount=0

w4 = item()
w4.name='body breastpiece'
w4.type='body armor'
w4.dexpen=0.03
w4.moves=[]
w4.chargeturn=0
w4.addchargeneed=0
w4.equipplace=[3]
w4.defencechance=8
w4.defamount=2

w5 = item()
w5.name='body gloves'
w5.type='body armor'
w5.dexpen=0.01
w5.moves=[]
w5.chargeturn=0
w5.addchargeneed=0
w5.equipplace=[4]
w5.defencechance=3
w5.defamount=0

w6 = item()
w6.name='body legpiece'
w6.type='body armor'
w6.dexpen=0.02
w6.moves=[]
w6.chargeturn=0
w6.addchargeneed=0
w6.equipplace=[5]
w6.defencechance=5
w6.defamount=1

w7 = item()
w7.name='body boots'
w7.type='body armor'
w7.dexpen=0.01
w7.moves=[]
w7.chargeturn=0
w7.addchargeneed=0
w7.equipplace=[6]
w7.defencechance=4
w7.defamount=0
