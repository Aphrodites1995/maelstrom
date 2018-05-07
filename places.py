class place(object):
	def __init__(self):
		self.name=''
		self.nearplaces=[]
		self.ground=[]
		self.monsters=[]
		self.description='Description'
		self.newplayer=False
		#initialize
p1 = place()
p1.name='Ruby City'
p1.nearplaces=[2,3]
p1.monsters=[]
p1.description='You are at a small city, with merchants on either side. Somewhere in the distance, you hear the roar of wolves, but something seems wrong with the roar...'
p2 = place()
p2.name='Ruby Inn'
p2.nearplaces=[1]
p2.monsters=[]
p2.description='You walk into a Inn, which is free depsite the fact that you can actually safely rest here.'
p3 = place()
p3.name='Ruby Forests'
p3.nearplaces=[1,4]
p3.monsters=[1,2]
p3.description='You walk along a road, which many adventurers traversed before you, into a forest. The roar of wolves become louder, and you feel the presence of red eyes that watch your every movement...'
p4 = place()
p4.name='Ruby Countryside'
p4.nearplaces=[3,5]
p4.monsters=[1,2,2]
p4.description='You walk into a clearing, where the land is full of wild grass, and the flapping of wings is clearly heard. There is a tiny cave in the distance, and you know if you approach the beings inside will attack you...'
p5 = place()
p5.name='Witch Hideout'
p5.nearplaces=[4]
p5.monsters=[3]
p5.description='You are in a cave where the witch practices her philosphy, and you read the only book you can find that will teach you how to wield the wand...'
def save():
	savefile=open('saveplace.txt','w')
	#new saveplace txt
	for i in range(0,5,1):
		listtemp=[]
		#listtemp is the list of ground
		stringtemp="for j in p"+str(i+1)+""".ground:
	listtemp.append(j)"""
		exec(stringtemp)
		for j in listtemp:
                        #saves listtemp
			savefile.write(j)
			savefile.write('\n')
		savefile.write("-\n")
		#then adds - to seperate
		#the order of save is numerical for read and save
	savefile.close()
newplayer=False
#initialise newplayer
try:
	savefile=open('saveplace.txt','r')
	#open save
except IOError:
	#print('debug')
	newplayer=True
	#its newplayer
for i in range(0,5,1):
	if newplayer==False:
                #if it is not a newplayer
		while True:
			stringtemp=savefile.readline().replace('\n','')
			#reads the line in stringtemp
			if stringtemp=='-':
				break
			#change to another place
			else:
				stringtemptwo='p'+str(i+1)+'.ground.append(stringtemp)'
				#appends into the ground
				exec(stringtemptwo)

if newplayer==True:
	p1.ground=['w1']
	p2.ground=[]
	p3.ground=['w1','w1']
	p4.ground=['w2']
	p5.ground=[]
	p1.newplayer=False
#initializes new player
save()
