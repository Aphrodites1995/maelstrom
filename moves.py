class move(object):
    def __init__(self):
        self.name=''
        self.dmgmin=0
        self.dmgmax=0
        self.defence=0
        self.blockchance=0
        self.accuracy=0
        self.chargeneeded=0
        self.requirements=''
m1 = move()
m1.name='slap'
m1.dmgmin=1
m1.dmgmax=3
m1.defence=1
m1.blockchance=10
m1.accuracy=30
m1.chargeneeded=6
m1.requirements='none'

m2 = move()
m2.name='punch'
m2.dmgmin=1
m2.dmgmax=5
m2.defence=2
m2.blockchance=3
m2.accuracy=22
m2.chargeneeded=5
m2.requirements='none'

m3 = move()
m3.name='pummel'
m3.dmgmin=2
m3.dmgmax=5
m3.defence=1
m3.blockchance=5
m3.accuracy=43
m3.chargeneeded=8
m3.requirements='self.invlist[0:1]=[\'w1\',\'w1\']'