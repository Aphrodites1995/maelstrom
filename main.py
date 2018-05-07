import sys
import places
import random
import items
import monsters
import functions
class player(object):
	def __init__(self):
		self.position=''
		self.knownplaces=[]
		self.invlist=[]
		self.stats=[]
		self.newplayer=False
		try:
			savefile=open("save.txt","r")
			savefile.close()
		except OSError:
			savefile=open("save.txt","w")
			savefile.close()
			print('New Player?')
			self.position = 1
			self.knownplaces=[1,2,3,5]
			self.invlist=['w1','w1','w3','w4','w5','w6','w7']
			#body parts are implemented as a filler
			#first seven equip
			#wp1,wp2,head,body,gloves,pants,foot
			self.stats=[1,1,1,30,30,0]
			#attack,defence,dexerity,health,max health,gold
			self.save()
			self.newplayer=True
		if self.newplayer==False:
			savefile=open("save.txt","r")
			lengths=savefile.readline().replace("\n",'')
			self.position = str(savefile.readline().replace("\n",''))
			for i in range(0,int(lengths[0]),1):
				self.knownplaces.append(int(savefile.readline().replace("\n",'')))
			for i in range(0,int(lengths[1]),1):
				self.invlist.append(savefile.readline().replace("\n",''))
			for i in range(0,int(lengths[2]),1):
				self.stats.append(savefile.readline().replace("\n",''))
			savefile.close()
		#https://stackoverflow.com/questions/29845051/remove-unique-values-from-a-list-and-keep-only-duplicates
		#you saved it badly(int()) sogood, dunno how...unicode ofr backspace??? or anti \n???
		#so where is save.txt becaus3e reading a no file raises ioerror
		self.mode = 'standing'
		self.moveableplaces=[]
		self.moveableplacesword=[]
		self.looksurround=''
		self.foundplaceword=''
		self.lookgroundthings=[]
		self.inspectthing=1
		self.lookgroundthingsword=[]
		self.invinspectthing=''
		self.invinspectthingpos=0
		self.canequipwithoutreplace=False
		self.equippos=0
		self.enemy=''
		self.enemyequip=[]
		self.enemystats=[]
		self.enemyname=''
		self.charge=0
		self.addcharge=0
		self.usablemoves=[]
		self.move
		self.movecharge=0
		self.moveaccuracy=0
		self.dealtdamage=0
		self.enemymoves=[]
		self.enemymove=0
		self.foughtturns=0
		self.enemydealtdamage=0
		while True:
			self.stand()
	def stand(self):
		for i in range(0,3,1):
			self.addcharge+=self.stats[i]
			print("""1.Travel To Other Lands
2.Look For Items
3.Hunt Monsters
4.Discover New Lands
5.Look Around
6.Manage Equipment
7.Save Game
		""")
		while '' in self.invlist:
			self.invlist.remove('')
		self.standchoice=input('Its your choice.')
		try:
			self.standchoice=int(self.standchoice)
		except ValueError:
			self.standchoice=0
		if self.standchoice==1:
			print("\n\n")
			self.run()
		if self.standchoice==2:
			print("\n\n")
			self.lookground()
		if self.standchoice==3:
			print("\n\n")
			self.hunt()
		if self.standchoice==4:
			print("\n\n")
			self.find()
		if self.standchoice==5:
			print("\n\n")
			self.lookaround()
		if self.standchoice==6:
			print("\n\n")
			self.inv()
		if self.standchoice==7:
			print("\n\n")
			self.save()
	def run(self):
		stringtemp="self.moveableplaces=places."+"p"+str(self.position)+".nearplaces"
		exec(stringtemp)
		self.moveableplaces=self.moveableplaces+self.knownplaces
		#creates a union of two, then finds duplicates below
		#creates a new version of moveableplaces so deleting i will not affect the count
		for i in range(0,len(self.moveableplaces),1):
			self.moveableplaces[i]=int(self.moveableplaces[i])
		#makes the list all int
		stringtemp=self.moveableplaces[:]
		for i in stringtemp:
			if stringtemp.count(i) == 1:
				self.moveableplaces.remove(i)
		#removes the places the player could move to but he does not know, and the places that he knows but he's not near to
		for i in self.moveableplaces:
			if self.moveableplaces.count(i) > 1:
				self.moveableplaces.remove(i)
		#removes the duplicates of the player's actual moveable places because the plus created two versions of it
		for i in range(0,len(self.moveableplaces),1):
			self.moveableplacesword.append('errorifseen')
			#because you cannot do test=[] then test[1]='test1' list index out of range
			stringtemp="self.moveableplacesword[i]=places.p"+str(self.moveableplaces[i])+".name"
			exec(stringtemp)
		for i in range(0,len(self.moveableplaces),1):
			print(str(i+1)+"."+str(self.moveableplacesword[int(i)]))
		movechoice = input('Where will you move to?')
		stringtemp=True
		try:
			movechoice=int(movechoice)
		except ValueError:
			stringtemp=False
		if stringtemp==True:
			movechoice=self.moveableplaces[int(movechoice)-1]
			#wordify move choice
			
			self.position=movechoice
		print('\n\n')
	def lookground(self):
		stringtemp="self.lookgroundthings=places.p"+str(self.position)+".ground"
		#look in places to find what's on the ground
		exec(stringtemp)
		if self.lookgroundthings==[]:
			print("Nothing Found")
		for i in range(0,len(self.lookgroundthings),1):
			stringtemp="self.lookgroundthingsword[i]=items."+self.lookgroundthings[i]+".name"
			self.lookgroundthingsword.append("errorifseen")
			#takes the name from items
			exec(stringtemp)
			print(str(i+1)+'.'+self.lookgroundthingsword[i])
			#prints it
			#also, make it save the items in places
		if not(self.lookgroundthings==[]):
			stringtemp=input("Which one do you want to inspect?")
			self.inspectthing=self.lookgroundthings[int(stringtemp)-1]
			#takes the input then makes it be inspected
			print("\n\n")
			stringtemp="print(items."+self.inspectthing+".name)"
			#prints the inspected thing's word
			exec(stringtemp)
		
			stringtemp=input("Do you take it?(y/n)")
			if stringtemp=='y':
				#if input is yes, takes it
				stringtemp="places.p"+str(self.position)+".ground.remove(self.inspectthing)"
				#removes the selected item
				exec(stringtemp)
				self.invlist.append(self.inspectthing)
				#adds the selected item to items
		print('In Progress')
	def hunt(self):
		self.fight()
		#just fights
	def find(self):
		stringtemp=random.randint(0,3)
		if stringtemp==3:
			print("\n\n")
			self.fight()
			#1/4 fights
		else:
			stringtemp="self.moveableplaces=places."+"p"+str(self.position)+".nearplaces"
			#all near places into self.moveableplaces
			exec(stringtemp)
			for i in range(0,len(self.moveableplaces),1):
				#for every near place
				if self.moveableplaces[i] not in self.knownplaces:
					print("You Found A New Place!")
					self.position=self.moveableplaces[i]
					#puts the player there
					self.knownplaces.append(self.moveableplaces[i])
					#makes it known by player
					stringtemp="self.foundplaceword=places.p"+str(self.moveableplaces[i])+".name"
					#gets the word version for found place
					exec(stringtemp)
					print("You found the place "+self.foundplaceword)
					#prints it
					break
	def lookaround(self):
		stringtemp="self.looksurround=places.p"+str(self.position)+".description"
		#takes description
		exec(stringtemp)
		print(self.looksurround)
	def inv(self):
		for i in range(0,len(self.invlist),1):
			#for every inventory item
			stringtemp="print(str(i+1)+'.'+items."+self.invlist[i]+".name)"
			exec(stringtemp)
			#prints name
		stringtemp=input('Which one do you want to inspect?')
		self.invinspectthingpos=int(stringtemp)-1
		#sets position of inspected thing
		self.invinspectthing=str(self.invlist[int(stringtemp)-1])
		#sets the inspected thing (w1)
		stringtemp=input("""1.Equip This
2.Drop This""")
		if stringtemp=='1':
			if self.invinspectthingpos<7:
				print('You cannot equip an equipped item')
				#examples shown for invinspectthing=w1, invinspectthingpos=8, equippos=0
				self.stand()
			#w2,w1,w3,w4,w5,w6,w7,w1
			stringtemptwo="self.equippos=random.choice(items."+self.invinspectthing+".equipplace)"
			exec(stringtemptwo)
			stringtemptwo="self.invlist.append(self.invlist[self.equippos])"
			#w2,w1,w3,w4,w5,w6,w7,w1,w2
			exec(stringtemptwo)
			stringtemptwo="self.invlist[self.equippos]=self.invinspectthing"
			#w1,w1,w3,w4,w5,w6,w7,w1,w2
			exec(stringtemptwo)
			del(self.invlist[self.invinspectthingpos])
			#w1,w1,w3,w4,w5,w6,w7,w2
		elif stringtemp=='2':
			if self.invinspectthingpos<7 and self.invinspectthing not in ['w1','w3','w4','w5','w6','w7']:
				#you can't drop a body part
				stringtemptwo="places.p"+str(self.position)+".ground.append('"+self.invlist[self.invinspectthingpos]+"')"
				#adds the thing onto the ground
				exec(stringtemptwo)
				stringtemptwo="self.invlist[self.invinspectthingpos]='w'+'"+str(self.invinspectthingpos)+"'"
				#because the body parts concidence with their place w3's equipplace is 3
				exec(stringtemptwo)
				if self.invinspectthingpos==2:
					self.invlist[self.invinspectthingpos]='w1'
					stringtemptwo="places.p"+str(self.position)+".ground.append('w2')"
					exec(stringtemptwo)
					#the only such exception is the sharp claw, so add that
			elif self.invinspectthingpos>6:
				self.invlist.remove(self.invinspectthing)
				stringtemptwo="places.p"+str(self.position)+".ground.append(self.invinspectthing)"
				#if it is not a body part, just drop it
				exec(stringtemptwo)

	def save(self):
		savefile=open("save.txt","w+")
		#write new
		stringtemp=str(len(self.knownplaces))+str(len(self.invlist))+str(len(self.stats))
		#length of save
		savefile.write(stringtemp+"\n")
		#save that
		savefile.write(str(self.position)+"\n")
		#position and enverything else
		for i in range(0,len(self.knownplaces),1):
			savefile.write(str(self.knownplaces[i]))
			savefile.write("\n")
		for i in range(0,len(self.invlist),1):
			savefile.write(str(self.invlist[i]))
			savefile.write("\n")
		for i in range(0,len(self.stats),1):
			savefile.write(str(self.stats[i]))
			savefile.write("\n")
		#close
		savefile.close()
		places.save()
	def fight(self):
		self.foughtturns=0
		self.enemymoves=[]
		self.enemymove=0
		self.usablemoves=[]
		self.usablemovescharge=[]
		self.charge=0
		self.enemydealtdamage=0
		stringtemp="self.enemy=random.choice(places.p"+str(self.position)+".monsters)"
		exec(stringtemp)
		stringtemp="self.enemyequip=monsters.mo"+self.enemy+".equipment"
		exec(stringtemp)
		stringtemp="self.enemystats=monsters.mo"+self.enemy+".stats"
		exec(stringtemp)
		stringtemp="self.enemyname=monsters.mo"+self.enemy+".name"
		exec(stringtemp)
		self.charge=self.addcharge
		while True:
			self.foughtturns=self.foughtturns+1
			if self.enemystats[3]<=0:
				print("Your enemy died, its loot is scattered on the ground.")
				stringtemp="for i in monsters.mo"+self.enemy+""".drop:
	places.p"""+str(self.position)+".ground.append(monsters.mo"+self.enemy+".drop)"
				exec(stringtemp)
				self.stats[5]+=self.foughtturns
				break
			self.charge+=self.addcharge
			print("You are fighting with a "+self.enemyname+".")
			print("You have "+self.charge+" action points.")
			print("You have "+self.stats[3]+" health.")
			print("Your enemy has "+self.enemystats[3]+" health.")
			for i in [0,1]:
    				stringtemp="for j in items."+self.invlist[i]+""".moves:
        self.usablemoves.append(j)"""
                                exec(stringtemp)
			for i in range(0,len(self.usablemoves,1):
                stringtemp="print(str(i-1)+'. '+moves.m."+str(self.usablemoves[i])+".name+' ('+moves.m"+str(self.usablemoves[i])+".chargeneeded+')'"
                exec(stringtemp)
            self.move=input('What do you do now?')
            stringtemp="self.movecharge=moves.m"+self.move+".chargeneeded"
            exec(stringtemp)
            stringtemp="self.moveaccuracy=moves.m"+self.move+".accuracy"
            exec(stringtemp)
			if functions.chance(100,self.moveaccuracy,True,100-self.moveaccuracy,False):
				stringtemp="self.dealtdamage=random.randint(moves.m"+str(self.move)+".dmgmin,moves."+str(self.move)+".dmgmax)"
				exec(stringtemp)
				self.enemystats[3]=self.enemystats[3]-self.damage
				stringtemp="print('Your '+moves.m"+self.move+".name+' dealt '+str(self.dealtdamage)+' damage.')"
				exec(stringtemp)
			for i in [0,1]:
			stringtemp="for j in items.w"+self.enemyequip[i]+""".moves:
        self.enemymoves.append(items.w"""+self.enemyequip[i]+".moves[j])"
				exec(stringtemp)
			self.enemymove=random.choice(self.enemymoves)
		stringtemp="if functions.chance(100,moves.m"+str(self.enemymove)+".accuracy,True,100-moves.m"+str(self.enemymove)+""".accuracy,False):
        self.enemydealtdamage=random.randint(moves.m"""+str(self.enemymove)+".dmgmin,moves.m"+str(self.enemymove)+""".dmgmax)
	self.stats[3]=self.stats[3]-self.enemydealtdamage
	print('You have been hit by'+moves.m"""+str(self.enemymove)+".name+' . It dealt '+self.enemydealtdamage+' damage.'"
				exec(stringtemp)
			print("Fighting is not yet implemented")
test = player()
