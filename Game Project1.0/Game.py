from tkinter import *
import csv
import random
window = Tk()
window.title("Treasure Hunter")
#playerfile setting
# global filepath, playerfile
# filepath = "player.csv"
# playerfile = open(filepath)

#img
playImg= PhotoImage(file="play.png")
pauseImg=PhotoImage(file="pause.png")
restartImg=PhotoImage(file="restart.png")
homeImg=PhotoImage(file="home.png")
leaderImg=PhotoImage(file="leadership.png")
iconhunterImg=PhotoImage(file="huntermed.png")
cheatImg=PhotoImage(file="cheat.png")
infoImg=PhotoImage(file="info.png")
running= True
#reset score&collide
resetscore = True
resetcollide = True
def gamescreen():
    global playground, collide, score, scoreLabel
    # Creating a canvas for the playground
    playground = Canvas(nameinputscreen, width=1280, height=720)
    playground.pack()

    #Playground background
    backgroundImg = PhotoImage(file="bg1.png")
    bg= playground.create_image(450,450,image=backgroundImg)

    #Place objects in background
    hunterImg = PhotoImage(file="hunter.png")
    hunter = playground.create_image(300,500,image=hunterImg)
    heartImg = PhotoImage(file="heart.png")
    heart = playground.create_image(100,300, image=heartImg)
    bombImg = PhotoImage(file="bomb.png")
    bomb = playground.create_image(800,450,image=bombImg)
    knifeImg = PhotoImage(file="knife.png")
    knife = playground.create_image(550, 550, image=knifeImg)
    shieldImg = PhotoImage(file="shield.png")
    shield = playground.create_image(250, 300, image=shieldImg)
    goldblockImg = PhotoImage(file="goldblock.png")
    goldblock = playground.create_image(330, 330, image=goldblockImg)
    goldboxImg = PhotoImage(file="goldbox.png")
    goldbox = playground.create_image(220, 220, image=goldboxImg)
    icegoldImg = PhotoImage(file="icegold.png")
    icegold = playground.create_image(660, 660, image=icegoldImg)


    #moving objects randomly
    def Randomheart():
        heartX=random.randint(30,1200)
        heartY=random.randint(65,650)
        playground.coords(heart,heartX,heartY)
    def Randombomb():
        bombX = random.randint(30, 1200)
        bombY = random.randint(65, 650)
        playground.coords(bomb, bombX, bombY)
    def Randomknife():
        knifeX = random.randint(30, 1200)
        knifeY = random.randint(65, 650)
        playground.coords(knife, knifeX, knifeY)
    def Randomshield():
        shieldX = random.randint(30, 1200)
        shieldY = random.randint(65, 650)
        playground.coords(shield, shieldX, shieldY)
    def Randomgoldbox():
        goldboxX = random.randint(30, 1200)
        goldboxY = random.randint(65, 650)
        playground.coords(goldbox, goldboxX, goldboxY)
    def Randomgoldblock():
        goldblockX = random.randint(30, 1200)
        goldblockY = random.randint(65, 650)
        playground.coords(goldblock, goldblockX, goldblockY)
    def Randomicegold():
        icegoldX = random.randint(30, 1200)
        icegoldY = random.randint(65, 650)
        playground.coords(icegold, icegoldX, icegoldY)

    #make objects move continuously and wont drive the game crazy
    def continuousmoveheart():
        if running:
            playground.move(heart, 6, 8)
            if playground.bbox(heart)[2]>1280 or playground.bbox(heart)[0]<0 or playground.bbox(heart)[1] < 0 or playground.bbox(heart)[2] >720:
                Randomheart()
                continuousmoveheart()
            else:
                playground.after(100, continuousmoveheart)
    def continuousmovebomb():
        if running:
            playground.move(bomb, -6, -9)
            if playground.bbox(bomb)[2] > 1280 or playground.bbox(bomb)[0] < 0 or playground.bbox(bomb)[1] < 0 or playground.bbox(bomb)[2] > 720:
                Randombomb()
                continuousmovebomb()
            else:
                playground.after(80,continuousmovebomb)
    def continuousmoveknife():
        if running:
            playground.move(knife,5, -6)
            if playground.bbox(knife)[2] > 1280 or playground.bbox(knife)[0] < 0 or playground.bbox(knife)[1] < 0 or playground.bbox(knife)[2] > 720:
                Randomknife()
                continuousmoveknife()
            else:
                playground.after(100,continuousmoveknife)
    def continuousmoveshield():
        if running:
            playground.move(shield,8, -9)
            if playground.bbox(shield)[2] > 1280 or playground.bbox(shield)[0] < 0 or playground.bbox(shield)[1] < 0 or playground.bbox(shield)[2] > 720:
                Randomshield()
                continuousmoveshield()
            else:
                playground.after(100,continuousmoveshield)
    def continuousmovegoldbox():
        if running:
            playground.move(goldbox,-5,0)
            if playground.bbox(goldbox)[2] > 1280 or playground.bbox(goldbox)[0] < 0 or playground.bbox(goldbox)[1] < 0 or playground.bbox(goldbox)[2] > 720:
                Randomgoldbox()
                continuousmovegoldbox()
            else:
                playground.after(100, continuousmovegoldbox)
    def continuousmovegoldblock():
        if running:
            playground.move(goldblock,0,-3)
            if playground.bbox(goldblock)[2] > 1280 or playground.bbox(goldblock)[0] < 0 or playground.bbox(goldblock)[1] < 0 or playground.bbox(goldblock)[2] > 720:
                Randomgoldblock()
                continuousmovegoldblock()
            else:
                playground.after(100, continuousmovegoldblock)
    def continuousmoveicegold():
        if running:
            playground.move(icegold,-5,0)
            if playground.bbox(icegold)[2] > 1280 or playground.bbox(icegold)[0] < 0 or playground.bbox(icegold)[1] < 0 or playground.bbox(icegold)[2] > 720:
                Randomicegold()
                continuousmoveicegold()
            else:
                playground.after(100, continuousmoveicegold)

    #starting the game, objects start random motion
    def startgame():
        global running, score, scoreLabel, collide
        running = True
        pauseButton = Button(playground, image=pauseImg, bg="#ae7046", height=70, width=70, command=pause)
        pauseButton.place(x=500, y=20)
        keyboard()#wake up the keyboard so they can be used once we press start
        playButton.destroy()
        continuousmoveheart()
        continuousmoveicegold()
        continuousmoveshield()
        continuousmoveknife()
        continuousmovebomb()
        continuousmovegoldblock()
        continuousmovegoldbox()
        if resetscore is True:
            score = 0
            scoreLabel = Label(playground, text="Score: " + str(score), font="Times 20 italic bold", bg="#ae7046",
                               fg="black")
            scoreLabel.place(x=620, y=20)
        if resetcollide is True:
            collide = 0
    #boundary boxes
    def hunterReachEdge():
        global hunterboundary
        hunterboundary = playground.bbox(hunter) #bbox is the boundary box
        if hunterboundary[0]<0:
            playground.move(hunter,15,0)
        elif hunterboundary[2]>1280:
            playground.move(hunter, -15, 0)
        elif hunterboundary[1]<50:
            playground.move(hunter, 0, 15)
        elif hunterboundary[3]>720:
            playground.move(hunter, 0, -15)
    #Collision detection(if collide, gain score, lose score or even gameover)
    #def pause():
    #def gameover():
    def collideobjects():
        global score
        HB = playground.bbox(heart)
        SL = playground.bbox(shield)
        KN = playground.bbox(knife)
        GBL = playground.bbox(goldblock)
        GBX = playground.bbox(goldbox)
        IG = playground.bbox(icegold)
        BB = playground.bbox(bomb)
        #collide with heart
        if hunterboundary[0]<HB[2]<hunterboundary[2] and hunterboundary[1]<HB[1]<hunterboundary[3]: #左下角
            Randomheart()
            score += 5
            scoreLabel.config(text="Score: "+str(score), fg="lightblue")
        elif hunterboundary[0] < HB[0] < hunterboundary[2] and hunterboundary[1]<HB[1]<hunterboundary[3]:#右下角
            Randomheart()
            score += 5
            scoreLabel.config(text="Score: " + str(score), fg="lightblue")
        elif hunterboundary[0] < HB[2] < hunterboundary[2] and hunterboundary[1] < HB[3] < hunterboundary[3]:#左上角
            Randomheart()
            score += 5
            scoreLabel.config(text="Score: " + str(score), fg="lightblue")
        elif hunterboundary[0] < HB[0] < hunterboundary[2] and hunterboundary[1]<HB[3]<hunterboundary[3]:#右上角
            Randomheart()
            score += 5
            scoreLabel.config(text="Score: " + str(score), fg="lightblue")
        #collide with knife
        if hunterboundary[0]<KN[2]<hunterboundary[2] and hunterboundary[1]<KN[1]<hunterboundary[3]: #左下角
            Randomknife()
            score += 30
            scoreLabel.config(text="Score: "+str(score),fg="orange")
        elif hunterboundary[0] < KN[0] < hunterboundary[2] and hunterboundary[1]<KN[1]<hunterboundary[3]:#右下角
            Randomknife()
            score += 30
            scoreLabel.config(text="Score: " + str(score), fg="orange")
        elif hunterboundary[0] < KN[2] < hunterboundary[2] and hunterboundary[1] < KN[3] < hunterboundary[3]:#左上角
            Randomknife()
            score += 30
            scoreLabel.config(text="Score: " + str(score), fg="orange")
        elif hunterboundary[0] < KN[0] < hunterboundary[2] and hunterboundary[1]<KN[3]<hunterboundary[3]:#右上角
            Randomknife()
            score += 30
            scoreLabel.config(text="Score: " + str(score), fg="orange")
        #collide with shield
        if hunterboundary[0]<SL[2]<hunterboundary[2] and hunterboundary[1]<SL[1]<hunterboundary[3]: #左下角
            Randomshield()
            score += 15
            scoreLabel.config(text="Score: "+str(score),fg="grey")
        elif hunterboundary[0] < SL[0] < hunterboundary[2] and hunterboundary[1]<SL[1]<hunterboundary[3]:#右下角
            Randomshield()
            score += 15
            scoreLabel.config(text="Score: " + str(score), fg="grey")
        elif hunterboundary[0] < SL[2] < hunterboundary[2] and hunterboundary[1] < SL[3] < hunterboundary[3]:#左上角
            Randomshield()
            score += 15
            scoreLabel.config(text="Score: " + str(score), fg="grey")
        elif hunterboundary[0] < SL[0] < hunterboundary[2] and hunterboundary[1]<SL[3]<hunterboundary[3]:#右上角
            Randomshield()
            score += 15
            scoreLabel.config(text="Score: " + str(score), fg="grey")
        #collide with goldbox
        if hunterboundary[0]<GBX[2]<hunterboundary[2] and hunterboundary[1]<GBX[1]<hunterboundary[3]: #左下角
            Randomgoldbox()
            score += 20
            scoreLabel.config(text="Score: "+str(score), fg="blue")
        elif hunterboundary[0] < GBX[0] < hunterboundary[2] and hunterboundary[1]<GBX[1]<hunterboundary[3]:#右下角
            Randomgoldbox()
            score += 20
            scoreLabel.config(text="Score: " + str(score), fg="blue")
        elif hunterboundary[0] < GBX[2] < hunterboundary[2] and hunterboundary[1] < GBX[3] < hunterboundary[3]:#左上角
            Randomgoldbox()
            score += 20
            scoreLabel.config(text="Score: " + str(score), fg="blue")
        elif hunterboundary[0] < GBX[0] < hunterboundary[2] and hunterboundary[1]<GBX[3]<hunterboundary[3]:#右上角
            Randomgoldbox()
            score += 20
            scoreLabel.config(text="Score: " + str(score), fg="blue")
        #collide with goldblock
        if hunterboundary[0]<GBL[2]<hunterboundary[2] and hunterboundary[1]<GBL[1]<hunterboundary[3]: #左下角
            Randomgoldblock()
            score += 35
            scoreLabel.config(text="Score: "+str(score), fg="#ffb500")
        elif hunterboundary[0] < GBL[0] < hunterboundary[2] and hunterboundary[1]<GBL[1]<hunterboundary[3]:#右下角
            Randomgoldblock()
            score += 35
            scoreLabel.config(text="Score: " + str(score), fg="#ffb500")
        elif hunterboundary[0] < GBL[2] < hunterboundary[2] and hunterboundary[1] < GBL[3] < hunterboundary[3]:#左上角
            Randomgoldblock()
            score += 35
            scoreLabel.config(text="Score: " + str(score), fg="#ffb500")
        elif hunterboundary[0] < GBL[0] < hunterboundary[2] and hunterboundary[1]<GBL[3]<hunterboundary[3]:#右上角
            Randomgoldblock()
            score += 35
            scoreLabel.config(text="Score: " + str(score), fg="#ffb500")
        #collide with icegold
        if hunterboundary[0]<IG[2]<hunterboundary[2] and hunterboundary[1]<IG[1]<hunterboundary[3]: #左下角
            Randomicegold()
            score += 40
            scoreLabel.config(text="Score: "+str(score), fg="#2bbcff")
        elif hunterboundary[0] < IG[0] < hunterboundary[2] and hunterboundary[1]<IG[1]<hunterboundary[3]:#右下角
            Randomicegold()
            score += 40
            scoreLabel.config(text="Score: " + str(score), fg="#2bbcff")
        elif hunterboundary[0] < IG[2] < hunterboundary[2] and hunterboundary[1] < IG[3] < hunterboundary[3]:#左上角
            Randomicegold()
            score += 40
            scoreLabel.config(text="Score: " + str(score), fg="#2bbcff")
        elif hunterboundary[0] < IG[0] < hunterboundary[2] and hunterboundary[1]<IG[3]<hunterboundary[3]:#右上角
            Randomicegold()
            score += 40
            scoreLabel.config(text="Score: " + str(score), fg="#2bbcff")
        #collide with bomb
        global collide
        if collide < 5 and score >=0:
            if hunterboundary[0]<BB[2]<hunterboundary[2] and hunterboundary[1]<BB[1]<hunterboundary[3]: #左下角
                Randombomb()
                if collide == 1:
                    score -= 100
                if collide == 2:
                    score -=200
                if collide == 3:
                    score -= 300
                if collide == 4:
                    score -= 400
                collide += 1
                scoreLabel.config(text="Score: "+str(score), fg="#ff1100")
            elif hunterboundary[0] < BB[0] < hunterboundary[2] and hunterboundary[1]<BB[1]<hunterboundary[3]:#右下角
                Randombomb()
                if collide == 1:
                    score -= 100
                if collide == 2:
                    score -= 200
                if collide == 3:
                    score -= 300
                if collide == 4:
                    score -= 400
                collide += 1
                scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
            elif hunterboundary[0] < BB[2] < hunterboundary[2] and hunterboundary[1] < BB[3] < hunterboundary[3]:#左上角
                Randombomb()
                if collide == 1:
                    score -= 100
                if collide == 2:
                    score -= 200
                if collide == 3:
                    score -= 300
                if collide == 4:
                    score -= 400
                collide += 1
                scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
            elif hunterboundary[0] < BB[0] < hunterboundary[2] and hunterboundary[1]<BB[3]<hunterboundary[3]:#右上角
                Randombomb()
                if collide == 1:
                    score -= 100
                if collide == 2:
                    score -= 200
                if collide == 3:
                    score -= 300
                if collide == 4:
                    score -= 400
                collide += 1
                scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
        else:
            gameover()
    # Move the hunter in directions（define movements)
    def moveright(event):
        if running:
            playground.move(hunter, 15, 0)  # move the truck 10 units to the right
            hunterReachEdge() #everytime we move the hunter we call this EdgeReach function
            collideobjects()
    def moveleft(event):
        if running:
            playground.move(hunter, -15, 0)  # move the truck 10 units to the left
            hunterReachEdge()
            collideobjects()
    def moveup(event):
        if running:
            playground.move(hunter, 0, -15)  # move up the truck 10 units
            hunterReachEdge()
            collideobjects()
    def movedown(event):
        if running:
            playground.move(hunter, 0, 15)  # move down the truck 10 units
            hunterReachEdge()
            collideobjects()




    # Making the hunter move
    def keyboard():
        playground.bind_all("<Right>", moveright)
        playground.bind_all("<d>", moveright)
        playground.bind_all("<Left>", moveleft)
        playground.bind_all("<a>", moveleft)
        playground.bind_all("<Up>", moveup)
        playground.bind_all("<w>", moveup)
        playground.bind_all("<Down>", movedown)
        playground.bind_all("<s>", movedown)
    #Pause the game
    def pause():
        global running, pausescreen, backgroundImg
        running = False
        pausescreen = Canvas(playground, width=1280, height=720)
        pausescreen.pack()
        backgroundImg = PhotoImage(file="bg1.png")
        bg = pausescreen.create_image(450, 450, image=backgroundImg)
        pauseword = Label(pausescreen, text="Paused", font="Algerian 48", fg="black", bg="#ae7046")
        pauseword.place(x=500, y=100)
        resumeButton = Button(pausescreen, text="Resume", font="Algerian 20", fg="orange", bg="#ae7046",command=resume)
        resumeButton.place(x=550, y=200)
        homeButton = Button(pausescreen, text="Home", font="Algerian 20", fg="orange", bg="#ae7046", command=endgame)
        homeButton.place(x=550, y=270)
        restartbutton = Button(pausescreen, image=restartImg, command=restartfrompause, bg="#ae7046", height=110, width=110)
        restartbutton.place(x=550, y=360)
    #Resume the game
    def resume():
        global score, scoreLabel, resetscore
        resetscore = False
        resetcollide = False
        pausescreen.destroy()
        startgame()
    #End the game( need to save score and playername)
    def endgame(): #back to home
        global score, scoreLabel, resetscore,collide,nameinputscreen
        nameinputscreen.destroy()
        resetscore = True
        collide = 0
        writescore()
    #Gameover when collide with bomb
    def gameover():
        global running, backgroundImg, gameoverscreen
        #save username and score
        running = False
        gameoverscreen = Canvas(playground, width=1280, height=720)
        gameoverscreen.pack()
        backgroundImg = PhotoImage(file="bg1.png")
        bg = gameoverscreen.create_image(450, 450, image=backgroundImg)
        gameoverword = Label(gameoverscreen, text="Game Over!", font="Algerian 50", fg="red", bg="#ae7046")
        gameoverword.place(x=450, y=100)
        restartbutton = Button(gameoverscreen, image=restartImg, command = restartfromgameover, bg="#ae7046", height=110, width=110 )
        restartbutton.place(x=550, y=360)
        homeButton = Button(gameoverscreen, text="Home", font="Algerian 20", fg="orange", bg="#ae7046", command=endgame)
        homeButton.place(x=550, y=270)
        writescore()
    #Restart the game after game over
    def restartfromgameover():
        global score, scoreLabel, gameoverscreen, resetcollide
        gameoverscreen.destroy()
        scoreLabel.destroy()
        resetcollide = True
        startgame()
    def restartfrompause():
        global score, scoreLabel, gameoverscreen, resetcollide
        pausescreen.destroy()
        scoreLabel.destroy()
        resetcollide = True
        startgame()





    #buttons
    playButton = Button(playground, text="Play", font="Algerian 20", fg="orange", bg="#ae7046", command = startgame)
    playButton.place(x=300,y=20)


    playground.mainloop()

def startscreen():
    global menu
    menu = Canvas(window, width=1280, height =720)
    menu.pack()
    #Titile
    title = Label(menu,text="Welcome to Treasure Hunter!", font="Algerian 24", fg="black", bg="#ae7046")
    title.place(x=640,y=30, anchor="center")
    #background
    backgroundImg = PhotoImage(file="bg1.png")
    bg = menu.create_image(450, 450, image=backgroundImg)
    #object
    iconhunter = menu.create_image(0, 50, image=iconhunterImg, anchor="nw")
    def moveicon():
        menu.move(iconhunter, 6, 0)
        if menu.bbox(iconhunter)[0] > 1280:
            menu.coords(iconhunter,0, 50)
            moveicon()
        else:
            menu.after(100, moveicon)
    moveicon()

    #Buttons
    StartButton = Button(menu, image=playImg, command = playerinputscreen, bg="#ae7046", height=110, width=110) #click startbutton to call the gamescreen  function
    StartButton.place(x=150,y=250)
    leaderboardButton = Button(menu, image=leaderImg, command = leaderboardscreen, bg="#ae7046", height=110, width=110)
    leaderboardButton.place(x=300, y=250)
    cheatButton = Button(menu, image=cheatImg, command = cheatscreen, bg="#ae7046", height=110, width=110)
    cheatButton.place(x=150, y=400)
    infoButton = Button(menu, image=infoImg, command=cheatscreen, bg="#ae7046", height=110, width=110)
    infoButton.place(x=300, y=400)



    menu.mainloop()

#leadershipboardscreen
def leaderboardscreen():
    leaderboard = Canvas(menu, width=1280, height =720)
    leaderboard.pack()
#cheat screen
def cheatscreen():
    cheat = Canvas(menu, width=1280, height =720)
    cheat.pack()

#playernameinput
def playerinputscreen():
    global nameinputscreen, backgroundImg, playernameentry
    nameinputscreen = Canvas(menu, width=1280, height=720)
    nameinputscreen.pack()
    # Titile
    title = Label(nameinputscreen, text="Please enter player name", font="Algerian 24", fg="black", bg="#ae7046")
    title.place(x=640, y=30, anchor="center")
    # background
    backgroundImg = PhotoImage(file="bg1.png")
    bg = nameinputscreen.create_image(450, 450, image=backgroundImg)
    #input box
    playernameentry = Entry(nameinputscreen)
    playernameentry.configure(bg="#ae7046", fg="black", font="Arial 24")
    nameinputscreen.create_window(600, 200, window=playernameentry, height=40, width=800)
    startgameButton = Button(nameinputscreen, text="Start", font="Algerian 24", fg="black", bg="#ae7046", command=gamescreen)  # click startbutton to call the gamescreen  function
    startgameButton.place(x=500, y=400)
    savenameButton = Button(nameinputscreen, text="Save", font="Algerian 24", fg="black", bg="#ae7046",command=writename)  # click startbutton to call the gamescreen  function
    savenameButton.place(x=500, y=300)

#write name to csv file
def writename():
    global playername,playerfile, playernameentry
    # fieldnames = ['Player', 'Score']
    # write_name = csv.writer(playerfile)
    # write_name.writerow(playername)
    playername = playernameentry.get()
    print(playername)
    with open("player.csv", 'a') as csvfile:
        fieldnames =['Player','Score']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({'Player':playername} )
    csvfile.close()

def writescore():
    global score
    with open("player.csv", 'a') as csvfile:
        fieldnames =['Player','Score']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({'Score':score} )
    csvfile.close()



def infoscreen():
    info = Canvas(menu, width=1280, height =720)
    info.pack()






startscreen()


