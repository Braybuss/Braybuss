from random import *

#Made by Braydon M(Braybuss)
#-------clear------------
def clear():
    lines = 15
    while lines > 1:
        print("\n")
        lines -= 1


#--------------takes the save slot to use
def saveslotchekr():
    global savenum
    savenumselec = False
    while savenumselec == False:
        try:
            savenum = int(input("save slot one, two or three?"))
        except ValueError:
            print("invalid input, please enter and integer")
        else:
            savenumselec = True
            
#-----------------------loads save(cannot due, imports cannot be run at modular level)



#---------------------select difficulty-----------
def difficultyselect():
    global easy
    global hard
    difficultyselec = False
    while difficultyselec == False:
        difficulty = input("quick play(easy and shorter game(q or e)) or long play(longer and more difficult version of the game(l or h))")
        if difficulty == "e" or difficulty == "q":
            print("quick play")
            easy = True
            hard = False
            difficultyselec = True

        elif difficulty == "l" or difficulty == "h":
            print("long game")
            easy = False
            hard = True
            difficultyselec = True
        else:
            print("invalid input, try again")
    print("difficulty selected")

#----------------------text that goes into the sace(stored variables)(0got rid of)

#------------------------save---------------------
def dosave(savenum):
    txt = open("save{0}.py".format(savenum), "w")
    txt.write("houses = {0}\nmine = {1}\nwell = {2}\nsmithy = {3}\nkitchen = {4}\nescavator = {5}\nfish_boiler = {6}\naluminumhouse = {7}\nfuel_pump = {8}\ndrill = {9}\n".format(houses,mine,well,smithy,kitchen,escavator,fish_boiler,aluminumhouse,fuel_pump,drill))#buildings
    txt.write("water = {0}\nfood = {1}\nlumber = {2}\nstone = {3}\niron = {4}\naluminum = {5}\ntitanium = {6}\nfuel = {7}\n".format(water,food,lumber,stone,iron,aluminum,titanium,fuel))#items
    txt.write("population = {0}\npopgain = {1}\nturn = {2}\nname = '{3}'\npoplost = {4}\nworkable = {5}\n".format(population,popgain,turn,name,poplost,workable))#other
    txt.write("tfood = {0}\ntwater = {1}\nkfood = {2}\nt200f = {3}\nt200w = {4}\nextraw = {5}\nextraf = {6}\n".format(tfood,twater,kfood,t200f,t200w,extraw,extraf))    
    if hard == True:
        txt.write("hard = True\neasy = False\nthruster = {0}\nfuel_tank = {1}\nrocket_shell = {2}\nrocket = {3}\nlaunchpad = {4}\n".format(thruster,fuel_tank,rocket_shell,rocket,launchpad))#hard items
        txt.close()
    if easy == True:
        txt.write("easy = True\nhard = False\nrocket = {0}\n".format(rocket))
        txt.close()
    print("game saved to slot {0}".format(savenum))


#---------------rand event gain
def gainz():
    global gain
    print("you can gain:\nwater + 40\nfood + 12\nlumber + 10\n")
    if mine > 0:
        print("stone + 7")
    if smithy > 0:
        print("iron + 2")
    if escavator > 0:
        print("aluminum + 1")
    if drill > 0:
        print("the treader does not have titanium")
    
    gain = input("what resource will you gain?")
    if gain == "w" or gain == "water":
        water += 40
    elif gain == "f" or gain == "food":
        food += 12
    elif gain == "l" or gain == "lumber":
        lumber += 10
    elif gain == "p" or gain == "population" or gain == "people":
        population += 2
    elif gain == "s" or gain == "stone":
        stone += 7
    elif gain == "a" or gain == "aluminum":
        aluminum += 1
    elif gain == "i" or gain == "iron":
        iron += 2
#-------------------------trading with barterer
def barter():
    if input("A Barterer has come to your settlment, would you like to trade?(y/n)") == "y":
        print("you can trade:\nwater(-45)\nfood(-15)\nlumber(-12)\n")
        if mine > 0:
            print("stone(-9)")
        if smithy > 0:
            print("iron(-3)")
        if escavator > 0:
            print("aluminium(-1)")
        if drill > 0:
            print("titanium(-1)")

        if fuel_pump > 0:
            print("you cannot trade fuel")

        give = input("what resource do you give?")
        if give == "f" or give == "food":
            if food >= 15:
                food -= 15
                gainz()
            else:
                print("you do not have enough food to do this")
                    
        elif give == "w" or give == "water":
            if water > 45:
                print("you trade water")
                water -= 45
                gainz()
            else:
                print("you do not have enough water to trade")
        elif give == "l" or give == "lumber":
            if lumber > 11:
                print("you trade lumber")
                lumber -= 12
                gainz()
            else:
                print("you do not have enough lumber to trade")
        elif give == "p" or give == "population" or give == "people":
            population -= 2
            gainz()

        elif give == "stone" or give == "s":
            if stone > 8:
                stone -= 9
                gainz()

        elif give == "iron" or give == "i":
            if iron > 2:
                iron -= 3
                gainz
                    
        elif give == "aluminum" or give == "a":
            if aluminum > 0:
                aluminum -= 1
                gainz()
        else:
            print("you did not trade")     
    
#-----------random event----------------
def randevent():
    global population
    if population > 8 or turn > 10:
        event = 1 #randint(1,10)
        global food
        global water
        global lumber
        global stone
        global iron
        if event == 1 or event == 4 or event == 7:
            barter()   
        if event == 2:
            randgain = randint(1,5)
            print("A driving potato has delevered {0} more people to your setlment".format(randgain))
            population += randgain
        if event == 3:
            randloss = randint(0,round(population/4))
            print("A crazed human attacked your settlment, you lost {0} people(this does not count against your score)".format(randloss))
            population -= randloss

        if event == 5:
            print("haha soup, you gain some food")
            food += randint(1,round(population*1.5))

        if event == 6 or event == 8:
            print("a contractor has come to your settlement, and offers to build something using your resources for {0} lumber+ the cost of that building(this opens the build menue again)".format(population))
            if input("do you trade? (y/n)?") == "y":
                if lumber >= population:
                    lumber -= population
                    build()
                else:
                    print("you do not have enough wood to do so")
        
#-------------------fishy production---------
def fishyproduction():
    global lumber
    global food
    global water
    global fuel
    global fishyw
    global fishyf
    if fish_boiler > 0:
        fishyproduce = False
        while fishyproduce == False:
            woodorfuel = input("will the fish boilers use lumber or fuel(press enter to skip)?")
            if woodorfuel == "l" or woodorfuel == "lumber":
                if int(lumber) >= 5*fish_boiler:
                    fishyw = fish_boiler*randint(12,15)
                    fishyf = fish_boiler*randint(4,10)
                    lumber -= 5*fish_boiler
                    fishyproduce = True
                else:
                    print("you do not have enough wood to do this")
            elif woodorfuel == "f" or woodorfuel == "fuel":
                if fuel >= fish_boiler:
                    fishyw = fish_boiler*randint(12,15)
                    fishyf = fish_boiler*randint(4,10)
                    fuel -= fish_boiler
                    fishyproduce = True
                else:
                    print("you do not have enough fuel")
            elif woodorfuel == "":
                print("fish boiler production skiped")
                fishyproduce = True
                fishyw = 0
                fishyf = 0
            else:
                print("invalid selection, try again")


#-------------------------------extra food and water for higher turns and difficulty---
def extrawf():
    global t200f
    global t200w
    global aluminumhousep
    global extraf
    global extraw
    global population
    global escavatorp
    global housep
    global poplost
    extraw = 0
    extraf = 0

    if hard == True:
        extraw = randint(0,int(population/2))
        extraf = randint(0,round(int(population)/6))
        
    if turn == 200:
        t200f = 50
        t200w = 50
        print("Prepare for the ultimate challenge, people will now continue to eat and drink more and more, it will start small, but continue to grow, the buildings will also grow in cost")
    if turn >= 200:
        t200f += 50
        t200w += 50
        extraw += t200w
        extraf += t200f
        aluminumhousep[0] += 2
        aluminumhousep[1] += 2
        escavatorp += 2
        housep += 1
        
            
            
    if turn >= 175:
        if turn == 175:
            print("your people now consume triple the resources they used to")
        extraw += population * 3
        extraf += population

    if turn >= 150:
        if turn == 150:
            print("your people now consume double the water that they did befor")
                
        extraw += population * 2

    if turn >= 125:
        if turn == 125:
            print("your people now consume 2 extra food every turn")
        extraf += population

    if turn >= 100:
        global workable
        if turn == 100:
            print("now if you have homless people, they will start to die")
        if workable < population:
            print("some of your population has died due to homelessness, this does count against your score")
            popcramplost = round((population - workable)//2)
            print("you lost {0} people".format(popcramplost))
            poplost += popcramplost
            population -= popcramplost

    if turn >= 75:
        extraf += population
        print("It is now turn {0}, people will also eat an extra food".format(turn))

    if turn >= 50:
        if turn == 50:
            print("turn {0}, people are starting to drink more, all people will drink an extra water now".format(turn))
        extraw += population
            

    
#---------------daily consume/record-------------manages how much is consumed by people and produces by other sources
def consume(f,w):

    global population
    global tfood
    global twater
    global popgain
    global poplost
    global lumber
    global fuel
    global t200f
    global t200w
    global extraf
    global extraw
    global fishyf
    global fishyw

    fishyproduction()
    
    consumption = int(population+popgain)
    wcunsumption = int((population+popgain) * 3)
    extrawf()

    global water
    global food
    global well
    global kitchen
    global kfood
    global lost
    wellwater = well*randint(6,9)
    water += wellwater
    print ("on turn {0}:".format(turn))
    if well > 0:
        print("your wells produced {0} water".format(wellwater))
    if kitchen > 0:
        print("your kitchens produced {0} food".format(kfood))
    if fish_boiler > 0:
        print("your fish boiler produced {0} water and {1} food".format(fishyw,fishyf))
        
    print("your people produced {0} water".format(twater))
    print("your people produced {0} food".format(tfood))
    tfood = 0
    twater = 0


    

    water -= extraw
    if water < 0:
        water = 0
        lost += population
        popgain = 0
        population = 0
        water = 0
        print("all of your people have died of dehydration")
    if water - wcunsumption < 0:
        kept = water
        poplost += population - kept
        population = kept
        print("some of your people died of dehydration, you kept {0} people".format(kept))
    else:
        water -= wcunsumption
        print("your people drank {0} water, {1} extra water was drank".format(wcunsumption,extraw))





    food -= extraf
    if food < 0:
        food = 0
        lost += population
        popgain = 0
        population = 0
        food = 0
        print("")
    if food - consumption < 0:
        kept = food
        poplost += population - kept
        population = kept
        print("some of your people died of starvation, you kept {0} people".format(kept))
    else:
        food -= consumption
        print("your people ate {0} food, {1} extra food was eaten".format(consumption,extraf))
          


#---------------baby make----------- child get borneded
def babymake(house,pop):
    global population
    global houses
    global aluminumhouse
    global popgain
    print("{0} children have grown up to be able to work".format(popgain))
    population += popgain
    popgain = 0
    
    if (population+popgain)//4 < houses+(aluminumhouse*2):
        if turn <= 6:
            popgain = randint(1,3)
            print("you have {0} new child(ren) in your population".format(popgain))
 
        if turn > 6:
            popgain = randint(0,round(population/3))
            if popgain > 0:
                print("you have {0} new child(ren) in your population".format(popgain))

    


#-----------build---------------Lets player chose things to build on their turn
def build():
    print("this is the build menu, you can build things on your turn\n\n")
    global mine
    global smithy
    global lumber
    global stone
    global iron
    global well
    global rocket
    global escavator
    global kitchen
    global aluminum
    global aluminumhouse
    global drill
    global titanium
    global fuel_pump
    global fuel
    global fish_boiler
    global launchpad
    global houses  #current materials # you can build:\nhouse(increase housing by 4): 10 lumber\nmine(lets you collect stone): 15 lumber
    print("you have {0} lumber".format(lumber))
    if mine > 0:
        print("you have {0} stone".format(stone))
    if smithy > 0:
        print("you have {0} iron".format(iron))
    if escavator > 0:
        print("you have {0} aluminium".format(aluminum))
    if drill > 0:
        print("you have {0} titanium".format(titanium))
    if fuel_pump > 0:
        print("you have {0} fuel".format(fuel))
    
    
    print ("\n\nyou have {0} houses\nyou have {1} mines".format(houses,mine))    
    if mine > 0:
        print("you have {0} smithys\nyou have {1} wells".format(smithy,well))
    if smithy > 0:
        print("you have {0} kitchens\nyou have {1} escavators".format(kitchen,escavator))
    if escavator > 0:
        print("you have {0} fish boilers\nyou have {1} aluminum houses\nyou have {2} drills".format(fish_boiler,aluminumhouse,drill))
    if hard == True:
        if drill > 0:
            print("you have {0} fuel pumps".format(fuel_pump))
    if hard == True:
        if escavator > 0:
            global rocket_shell
            global thruster
            global fuel_tank
            print("\n\nrocket peices\nyou have {0} rocket shells(you need 1)\nyou have {1} thrusters(you need 3)\nyou have {2} fuel tanks(you need 2)".format(rocket_shell,thruster,fuel_tank))


        
    #options
    print("\n\nyou can build:\nhouse(increase housing by 4): {0} lumber\nmine(lets you collect stone(2 people per mine)): {1} lumber".format(housep,minep))    
    if mine > 0:
        print("well(produces 5=8 water every turn): {0} lumber {1} stone \nsmithy(lets you collect iron(1 person per smithy)): {2} stone".format(wellp[0],wellp[1], smithyp))
    if smithy > 0:
        print("kitchen(people who work here produce triple the food(1 per kitchen)): {0} lumber, {1} stone, {2} iron".format(kitchenp[0],kitchenp[1],kitchenp[2]))
    
        print("escavator(allows for the production of aluminum(3 people per escavator)): {0} iron\n".format(escavatorp))
    
    if easy == True:
        if smithy > 0:
            print("rocket: 30 iron(game win)\n\n")
    if hard == True:
        if smithy > 0:
            print("launchpad: {0} iron, peice of rocket".format(launchpadp))
        if escavator > 0:
            print("Rocket Shell: {0} aluminum, {1} titanium\nThruster: {2} iron {3} titanium\nFuel tank: {4} iron {5} fuel\n".format(rocket_shellp[0],rocket_shellp[1],thrusterp[0],thrusterp[1],fuel_tankp[0],fuel_tankp[1]))
    if escavator > 0:
        print("\nfish boiler(produces food and water,uses 5 wood or 1 fuel per day): {0} iron, {1} aluminum\naluminum house(can hold 8 people instead of 4): {2} wood, {3} aluminum\ndrill(allows for the production of titanium(5 people per drill)): {4} iron, {5} aluminum".format(fish_boilerp[0],fish_boilerp[1],aluminumhousep[0],aluminumhousep[1],drillp[0],drillp[1]))
    if drill > 0:
        print("fuel pump, allows for the collection of rocket fuel: {0} aluminum, {1} titanium\n".format(fuel_pumpp[0],fuel_pumpp[1]))
    if hard == True
        if rocket_shell > 0 and fuel_tank > 0 and thruster > 2 and launchpad > 0:
            print("ROCKET READY TO BUILD")
    




    #user decides what to build
    building = input("what would you like to build?(press enter to skip)\n>>>")
    if building == "house" or building == "h":
        if lumber >= 10:
            houses += 1
            print("you have built a house")
            lumber -= 10
        else:
            print("you do not have enough materials to build this")

    elif building == "mine" or building == "m":
        if lumber >= 15:
            mine += 1
            print("you have built a mine")
            lumber -= 15
        else:
            print("you do not have enough materials to build this")


    elif building == "well" or building == "w":
        if lumber >= wellp[0] and stone >= wellp[1]:
            well += 1
            print("you have built a well")
            lumber -= wellp[0]
            stone -= wellp[1]
        else:
            print("you do not have enough materials to build this")

    elif building == "smithy" or building == "s":
        if stone >= smithyp:
            smithy += 1
            print("you have built a smithy")
            stone -= smithyp
        else:
            print("you do not have enough materials to build this")

    elif building == "k" or building == "kitchen":
        if lumber >= kitchenp[0] and stone >= kitchenp[1] and iron >= kitchenp[2]:
            print("you built a kitchen")
            lumber -= kitchenp[0]
            stone -= kitchenp[1]
            iron -= kitchenp[2]
            kitchen += 1
        else:
            print("you do not have enoguh resources to build this")

    elif building == "d" or building == "drill":
        if iron >= drillp[0] and aluminum >= drillp[1]:
            print("you built a drill")
            iron -= drillp[0]
            aluminum -= drillp[1]
            drill += 1
        else:
            print("you do not have enoguh resources to build this")

    elif building == "rocket" or building == "r":
        if easy == True:
            if iron >= rocketp:
                rocket += 1
                print("you have built a rocket")
                iron -= 30
            else:
                print("you do not have enough materials to build this")
        elif hard == True:
            if rocket_shell > 0 and thruster > 2 and fuel_tank > 1 and launchpad > 0:
                print("you built a rocket")
                rocket +=1
                rocket_shell -= 1
                thruster -= 3
                fuel_tank -= 2
            else:
                print("you do not have enought resources to build this")

    elif building == "fb" or building == "fish boiler":
        if iron >= fish_boilerp[0] and aluminum >= fish_boilerp[1]:
            iron -= fish_boilerp[0]
            aluminum -= fish_boilerp[1]
            print("you have built a fish boiler")
            fish_boiler += 1
        else:
            print("you do not have enough materials to build this")

            

    elif building == "escavator" or building == "e":
        if iron >= escavatorp:
            iron -= escavatorp
            print("you have built an escavator")
            escavator += 1
        else:
            print("you do not have enough materials to build this")

    elif building == "a" or building == "aluminum house":
        if lumber >= aluminumhousep[0] and aluminum >= aluminumhousep[1]:
            aluminumhouse += 1
            lumber -= aluminumhousep[0]
            aluminum -= aluminumhousep[1]
            print("you build an aluminum house")
        else:
            print("you do not have enough resources to build this")



    elif building == "fp" or building == "fuel pump":
        if aluminum >= fuel_pumpp[0] and titanium >= fuel_pumpp[1]:
            fuel_pump += 1
            aluminum -= fuel_pumpp[0]
            titanium -= fuel_pumpp[1]
            print("you built a fuel pump")
        else:
            print("you do not have enough resources to build this")
    
        
    elif hard == True:
        if building == "l" or building == "launch pad": 
            if iron >= launchpadp:
                launchpad += 1
                print("you have built a Launch pad for the rocket")
                iron -= launchpadp
                
        elif building == "rs" or building == "rocket shell":
            if aluminum >= rocket_shellp[0] and titanium >= rocket_shellp[1]:
                print("you have built a rocket shell")
                rocket_shell += 1
                aluminum -= rocket_shellp[0]
                titanium -= rocket_shellp[1]
            else:
                print("you do not have enough resources to build this")
                
        elif building == "t" or building == "thruster":
            if iron >= thrusterp[0] and titanium >= thrusterp[1]:
                thruster += 1
                iron -= thrusterp[0]
                aluminum -= thrusterp[1]
                print("you built a thruster")
            else:
                print("you do not have enough resources to build this")



        elif building == "ft" or building == "fuel tank":
            if iron >= fuel_tankp[0] and fuel >= fuel_tankp[1]:
                fuel_tank += 1
                iron -= fuel_tankp[0]
                fuel -= fuel_tankp[1]
                print("you built a fuel tank")
            else:
                print("you do not have enough resources to build this")

        else:
            print("you did not build anything")
            if building != "":
                print("invalid input")
                build()
                           
    else:
        print("you did not build anything")
        if building != "":
            print("invalid input")
            build()

    
    









#----------produce------------ manages daily production, lets player decide what will be produced and how much
def produce():

    global tutorial
    global water
    global twater
    global food
    global tfood
    global lumber
    global stone
    global iron
    global kitchen
    global kfood
    global aluminum
    global titanium  
    global fuel
    global workable
    print("you can produce:\nwater (you have {0})\nfood (you have {1})\nlumber (you have {2})".format(water,food,lumber))
    global mine
    if mine > 0:
        print("stone (you have {0})".format(stone))
    global smithy
    if smithy > 0:
        print("iron (you have {0})".format(iron))
    if escavator > 0:
        print("aluminum (you have {0})".format(aluminum))
    if drill > 0:
        print("titanium (you have {0})".format(titanium))
    if fuel_pump > 0:
        print("fuel (you have {0})".format(fuel))
    global population
    if houses*4 + (aluminumhouse*8) < population:
        print("you have some homeless people, they cannot work")
        workable = houses*4 + aluminumhouse*8
    else:
        workable = population
    
    print("you have {0} people able to work".format(workable))


    
    if workable > 0:
        waterproduced = False
        if tutorial == True:
            print("Each person that produces water will produce 6-9 water befor the end of your turn. Type in the number, out of the workable population you have")
        while waterproduced == False:
            try:
                pwater = int(input("how many will produce water?"))
            except ValueError:
                print("invalid input, try again")
            else:
                waterproduced = True
                if pwater > workable:
                    print("you have to many people working here, the extras will not be counted")
                    pwater = workable
                    workable -= pwater
                else:
                    workable -= pwater

                while pwater > 0:
                    pwater -= 1
                    wproduced = randint(6,9)
                    water += wproduced
                    twater += wproduced

            


    if workable > 0:
        print("you have {0} people left to work".format(workable))
        if tutorial == True:
            print("each person that works here will produce 2-4 food a turn")
        foodproduced = False
        while foodproduced == False:
            try:
                pfood = int(input("how many will produce food?"))
            except ValueError:
                print("invalid input, try again")
            else:
                foodproduced = True
                if pfood > workable:
                    print("you have to many people working here, the extras will not be counted")
                    pfood = workable
                    workable -= pfood
                else:
                    workable -= pfood
                while pfood > 0:
                    pfood -= 1
                    fproduced = randint(2,4)
                    food += fproduced
                    tfood += fproduced
    else:
        print("you do not have enough people to produce food")



    if workable > 0:
        print("you have {0} people left to work".format(workable))
        lumberproduced = False
        while lumberproduced == False:
            try:
                plumber = int(input("how many will produce lumber?"))
            except ValueError:
                print("invalid input, try again")
            else:
                lumberproduced = True
        if plumber > workable:
            print("you have to many people working here, the extras will not be counted")
            plumber = workable
            workable -= plumber
        else:
            workable -= plumber
        while plumber > 0:
            plumber -= 1
            lumber += randint(2,5)
    else:
        print("you do not have anyone left to produce lumber")



    if workable > 0:
        if mine > 0:
            print("you have {0} people left to work".format(workable))
            stoneproduced = False
            while stoneproduced == False:
                try:
                    pstone = int(input("how many will produce stone(you can have a maximum of {0} do so)?".format(mine*2)))
                except ValueError:
                    print("invalid input, try again")
                else:
                    stoneproduced = True
                    if pstone > workable:
                        print("you have to many people working here, the extras will not be counted")
                        pstone = workable
                        workable -= pstone
                    elif pstone > mine*2:
                       print("you do not have enough space for that many workers, the extras will not be counted")
                       pstone = mine*2
                       workable -= pstone
                    
                    else:
                        workable -= pstone
                    while pstone > 0:
                        pstone -= 1
                        stone += randint(2,3)


    if smithy > 0:
        if workable == 0:
            print("you do not have anyone left to produce iron")
    if workable > 0:
        if smithy > 0:
            print("you have {0} people left to work".format(workable))
            ironproduced = False
            while ironproduced == False:
                try:
                    piron = int(input("how many will produce iron(you can have up to {0} people work to do so)?".format(smithy)))
                except ValueError:
                    print("invalid input, try again")
                else:
                    ironproduced = True
                    print("what happening")
            if piron > workable:
                print("you have to many people working here, the extras will not be counted")
                piron = workable
                workable -= piron
                ironproduced = True
            elif piron > smithy:
                print("you do not have enough space for that many workers, the extras will not be counted")
                piron = smithy
                workable -= piron
                ironproduced = True
                            
            else:
                workable -= piron
            ironproduced = True
            iron += (piron)*2
    kfood = 0
    if kitchen > 0:
        if workable == 0:
            print("you do not have enough people to work in the kitchen")
        if workable > 0:
            producedkfood = False
            while producedkfood == False:
                try:
                    pkfood = int(input("how many will produce food in the kitchen(you can have up to {0} people do so)?".format(kitchen)))
                except ValueError:
                    print("invalid input, try again")
                else:
                    producedkfood = True
                    if pkfood > workable:
                        print("you have to many people working here, the extras will not be counted")
                        pkfood = workable
                        workable -= pkfood
                    elif pkfood > kitchen:
                            print("you do not have enough space for that many workers, the extras will not be counted")
                            pkfood = kitchen
                            workable -= pkfood
                    else:
                        workable -= pkfood
                    kfood = 0
                    while pkfood > 0:
                        pkfood -= 1
                        kfood += randint(6,8)
                    food += kfood



    if escavator > 0:
        if workable == 0:
            print("you do not have anyone left to produce aluminum")
    if workable > 0:
        if escavator > 0:
            print("you have {0} people left to work".format(workable))
            alumproduced = False
            while alumproduced == False:
                try:
                    palum = int(input("how many will produce aluminum(you can have up to {0} people work to do so)?".format(escavator*3)))
                except ValueError:
                    print("invalid input, try again")
                else:
                    alumproduced = True
                    if palum > workable:
                        print("you have to many people working here, the extras will not be counted")
                        palum = workable
                        workable -= palum
                    elif palum > escavator*3:
                            print("you do not have enough space for that many workers, the extras will not be counted")
                            palum = escavator*3
                            workable -= palum
                            
                    else:
                        workable -= palum
                    aluminum += (palum)*randint(1,2)



    if drill > 0:
        if workable == 0:
            print("you do not have anyone left to produce titanium")
    if workable > 0:
        if drill > 0:
            print("you have {0} people left to work".format(workable))
            titaproduced = False
            while titaproduced == False:
                try:
                    ptita = int(input("how many will produce titanium(you can have up to {0} people work to do so)?".format(drill*5)))
                except ValueError:
                    print("invalid input, try again")
                else:
                    titaproduced = True
                    if ptita > workable:
                        print("you have to many people working here, the extras will not be counted")
                        ptita = workable
                        workable -= ptita
                    elif ptita > drill*5:
                            print("you do not have enough space for that many workers, the extras will not be counted")
                            ptita = drill
                            workable -= ptita
                            
                    else:
                        workable -= ptita
                    titanium += (ptita)



    if fuel_pump > 0:
        if workable == 0:
            print("you do not have anyone left to extract fuel")
    if workable > 0:
        if fuel_pump > 0:
            print("you have {0} people left to work".format(workable))
            fuelproduced = False
            while fuelproduced == False:
                try:
                    pfuel = int(input("how many will produce fuel(you can have up to {0} people work to do so)?".format(fuel_pump*2)))
                except ValueError:
                    print("invalid input, try again")
                else:
                    fuelproduced = True
                    if pfuel > workable:
                        print("you have to many people working here, the extras will not be counted")
                        pfuel = workable
                        workable -= pfuel
                    elif pfuel > fuel_pump*2:
                            print("you do not have enough space for that many workers, the extras will not be counted")
                            pfuel = fuel_pump*2
                            workable -= pfuel
                            
                    else:
                        workable -= pfuel
                    fuel += round((pfuel)*1.5)
    if houses*4 + (aluminumhouse*8) < population:
        workable = houses*4 + aluminumhouse*8
    else:
        workable = population

#-----------outerloop----------------
print("welcome to populosue!")
while input("start game?(y/n)\n>>>") != "n":
    easy = False
    hard = False
    save = input("load save(l), or new game?(n)")
    savenum = 0
    saveslotchekr()
#----------------This code has to be here because imports cannot be in a function
    if save == "l":
        if savenum == 1:
            try:
                from save1 import *
            except (ModuleNotFoundError,FileNotFoundError):
                print("you do not have a save here, new game instead")
                save = "n"
            else:
                print("succes")
        if savenum == 2:
            try:
                from save2 import *
            except (ModuleNotFoundError,FileNotFoundError):
                print("you do not have a save here, new game instead")
                save = "n"
            else:
                print("succes")
        if savenum == 3:
            try:
                from save3 import *
            except (ModuleNotFoundError,FileNotFoundError):
                print("you do not have a save here, new game instead")
                save = "n"
            else:
                print("succes")
        
#end of segment
    if save == "n":
        difficultyselect()
        name = input("what is your username?")

        if easy == True:
            food = 15

            water = 45

            population = 6

            houses = 2

            lumber = 8

        if hard == True:
            food = 12

            water = 35

            population = 5

            houses = 1

            lumber = 8

            launchpad = 0

        aluminumhousep = [15,30] #wood,aluminum


        turn = 0

        tfood = 0

        pfood = 0

        kfood = 0

        twater = 0

        pwater = 0

        mine = 0

        well = 0

        stone = 0

        smithy = 0

        kitchen = 0

        rocket = 0

        iron = 0

        escavator = 0

        aluminum = 0

        fish_boiler = 0

        aluminumhouse = 0

        drill = 0

        titanium = 0

        rocket_shell = 0

        fuel_pump = 0

        fuel = 0

        fuel_tank = 0

        thruster = 0

        popgain = 0

        poplost = 0

        t200f = 0

        t200w = 0

        workable = 4

        gain = "soup"

        if name == "testering":
            lumber = 200
            stone = 200
            iron = 200
            aluminum = 200
            titanium = 200
            fuel = 200
            smithy = 1
            escavator = 1
            drill = 1
            fuel_pump = 1

    

    if easy == True:
        housep = 10
        minep = 15
        wellp = [15,5]
        smithyp = 20
        kitchenp = [8,10,15]
        rocketp = 30
        escavatorp = 30
        drillp = [20,15]


    if hard == True:
        housep = 12
        minep = 18
        wellp = [16,8] #wood, stone
        smithyp = 24
        kitchenp = [12,15,20] #wood, stone, iron
        launchpadp = 45
        escavatorp = 32 #iron
        aluminumhousep = [16,32] #wood,aluminum
        drillp = [24,18] #iron, aluminum
        rocket_shellp = [45,30]#aluminum, titanium
        
    aluminumhousep = [15,30] #wood,aluminum
    fish_boilerp = [15,15] #iron, aluminum
    fuel_pumpp = [20,15]#almuminum, titanium
    fuel_tankp = [30,15]#iron, fuel
    thrusterp = [20,10]#iron, titanium
    

    gameover = False

    gamewin = False

    rocket = 0

    tutorial = False

    score = 0
    #-------------turn--------------
    turn += 1
    print("turn " + str(turn))
    if save == "n":
        if input("tutorial?(y/n)") == "y":
            tutorial = True
    if tutorial == True:
        print("you start with {0} people, they each consume one food and 3 water at the end of your turn. if they are all fed, and you have housing space left, you can have more children born".format(population))
    produce()
    fishyw = 0
    fishyf = 0
    extraw = 0
    extraf = 0
        
    clear()
    if tutorial == True:
        print ("now that you have produced, a summary will apear, your end goal is to build a rocket(you wont see it yet, but you can find out how to)")
        print("")
    consume(water,food)
    babymake(houses,population)
    print("press enter to continue on, good luck!")
    if tutorial == True:
        tutorial = False
    while input("end turn") != "n":
            clear()
            print("your settlemnt has {0} houses".format(houses))
            if aluminumhouse > 0:
                print("your population has {0} aluminum houses".format(aluminumhouse))
            turn += 1
            print("turn " + str(turn))
            print("your population is {0} adults and {1} children".format(population,popgain))
            produce()
            if input("would you like to open the build menu?(y/n)\n>>>") == "y":
                build()

            

            clear()
            randevent()
            
            consume(water,food)
            babymake(houses,population)
            dosave(savenum)




            if population <= 0:
                print("game over, everyone died")
                gameover = True
                if endless == True:
                    score = turn - poplost
                    print("you lost on turn {0}, with a population of {1}, you lost a total of {2} people, and your final score was {3}".format(turn,population,poplost,score))
                
            if gameover == True:
                print("you lasted " + str(turn) + " turns")
                break

            if rocket > 0:
                gamewin = True

            if gamewin == True:
                if easy == True:
                    print("You have won! you did this in {0} turns".format(turn))

                    score = 50 - turn + round(population/3) + round(popgain/3) - poplost
                    print("your score was {0}".format(score))
                    
                    txt = open('highscores.txt', 'a')
                    
                    txt.write("{0} won with a score of {1}, on turn {2}, with a population of {3} on quick play\n".format(name,score,turn,population))
                    txt.close()

                    

                if hard == True:
                    print("You have won! you did this in {0} turns".format(turn))

                    score = 100 - turn + round(population/2) + round(popgain/2) - poplost
                    print("your score was {0}".format(score))
                    
                    txt = open('highscores.txt', 'a')
                    
                    txt.write("{0} won with a score of {1}, on turn {2}, with a population of {3} on long play\n".format(name,score,turn,population))
                    txt.close()
                print("press enter to play in endless mode, or n to play again/quit")
                endless = True
                
            
            

        
