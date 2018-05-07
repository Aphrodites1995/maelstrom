class move(object):
    def __init__(self):
        self.name=''
        self.dmgmin=0
        self.dmgmax=0
        self.accuracy=0
        self.chargeneeded=0
        self.requirements=''
m1 = move()
m1.name='slap'
m1.dmgmin=1
m1.dmgmax=3
m1.accuracy=30
m1.chargeneeded=6
m1.requirements='True'

m2 = move()
m2.name='punch'
m2.dmgmin=1
m2.dmgmax=5
m2.accuracy=22
m2.chargeneeded=5
m2.requirements='True'

m3 = move()
m3.name='pummel'
m3.dmgmin=2
m3.dmgmax=5
m3.accuracy=43
m3.chargeneeded=8
m3.requirements='self.invlist[0:1]=[\'w1\',\'w1\']'

m4 = move()
m4.name='slash'
m4.dmgmin=1
m4.dmgmax=3
m4.accuracy=32
m4.chargeneeded=4
m4.requirements='True'

m5 = move()
m5.name='stab'
m5.dmgmin=3
m5.dmgmax=10
m5.accuracy=20
m5.chargeneeded=6
m5.requirements='True'

m6 = move()
m6.name='cross slash'
m6.dmgmin=3
m6.dmgmax=10
m6.accuracy=50
m6.chargeneeded=9
m6.requirements='self.invlist[0:1]=[\'w2\',\'w2\']'

m7 = move()
m7.name='fire'
m7.dmgmin=3
m7.dmgmax=3
m7.accuracy=50
m7.chargeneeded=4
m7.requirements='True'

m8 = move()
m8.name='magic missile'
m8.dmgmin=8
m8.dmgmax=20
m8.accuracy=20
m8.chargeneeded=12
m8.requirements='True'