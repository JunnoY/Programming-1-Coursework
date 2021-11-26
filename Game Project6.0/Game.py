from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv,random, webbrowser,operator
window = Tk()
window.title("Treasure Hunter")


#img
playImg= PhotoImage(file="play.png")
pauseImg=PhotoImage(file="pause.png")
restartImg=PhotoImage(file="restart.png")
homeImg=PhotoImage(file="home.png")
leaderImg=PhotoImage(file="leadership.png")
iconhunterImg=PhotoImage(file="huntermed.png")
cheatImg=PhotoImage(file="cheat.png")
infoImg=PhotoImage(file="info.png")
settingImg=PhotoImage(file="setting.png")
running= True
#reset score&collide
resetscore = True
resetcollide = True
#cheatingmode
GET1000FORFREE = False
KJ = False
Fullbombs = True
Allbombsoff= False
#keyboardsettings
deaultUp = True
deaultDown = True
deaultLeft = True
deaultRight = True
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
    bombImg = PhotoImage(file="bomb.png")
    if Allbombsoff is False and Fullbombs is True:
        bomb = playground.create_image(800, 450, image=bombImg)
        bomb1 = playground.create_image(800, 450, image=bombImg)
        bomb2 = playground.create_image(800, 300, image=bombImg)
        bomb3 = playground.create_image(450, 450, image=bombImg)
        bomb4 = playground.create_image(700, 450, image=bombImg)
        bomb5 = playground.create_image(600, 420, image=bombImg)
    elif Allbombsoff is False and Fullbombs is False:
        bomb3 = playground.create_image(450, 450, image=bombImg)
        bomb4 = playground.create_image(700, 450, image=bombImg)
        bomb5 = playground.create_image(600, 420, image=bombImg)


    #putting objects randomly
    def Randomheart():
        heartX=random.randint(30,1200)
        heartY=random.randint(65,650)
        playground.coords(heart,heartX,heartY)
    def Randombomb():
        bombX = random.randint(30, 1200)
        bombY = random.randint(65, 650)
        playground.coords(bomb, bombX, bombY)
    def Randombomb1():
        bomb1X = random.randint(30, 1200)
        bomb1Y = random.randint(65, 650)
        playground.coords(bomb1, bomb1X, bomb1Y)
    def Randombomb2():
        bomb2X = random.randint(30, 1200)
        bomb2Y = random.randint(65, 650)
        playground.coords(bomb2, bomb2X, bomb2Y)
    def Randombomb3():
        bomb3X = random.randint(30, 1200)
        bomb3Y = random.randint(65, 650)
        playground.coords(bomb3, bomb3X, bomb3Y)
    def Randombomb4():
        bomb4X = random.randint(30, 1200)
        bomb4Y = random.randint(65, 650)
        playground.coords(bomb4, bomb4X, bomb4Y)
    def Randombomb5():
        bomb5X = random.randint(30, 1200)
        bomb5Y = random.randint(65, 650)
        playground.coords(bomb5, bomb5X, bomb5Y)
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
    def continuousmovebomb1():
        if running:
            playground.move(bomb1, -4, -9)
            if playground.bbox(bomb1)[2] > 1280 or playground.bbox(bomb1)[0] < 0 or playground.bbox(bomb1)[1] < 0 or playground.bbox(bomb1)[2] > 720:
                Randombomb1()
                continuousmovebomb1()
            else:
                playground.after(80,continuousmovebomb1)
    def continuousmovebomb2():
        if running:
            playground.move(bomb2, -6, 9)
            if playground.bbox(bomb2)[2] > 1280 or playground.bbox(bomb2)[0] < 0 or playground.bbox(bomb2)[1] < 0 or playground.bbox(bomb2)[2] > 720:
                Randombomb2()
                continuousmovebomb2()
            else:
                playground.after(80,continuousmovebomb2)
    def continuousmovebomb3():
        if running:
            playground.move(bomb3, 5, -6)
            if playground.bbox(bomb3)[2] > 1280 or playground.bbox(bomb3)[0] < 0 or playground.bbox(bomb3)[1] < 0 or playground.bbox(bomb3)[2] > 720:
                Randombomb3()
                continuousmovebomb3()
            else:
                playground.after(80,continuousmovebomb3)
    def continuousmovebomb4():
        if running:
            playground.move(bomb4, 3, -10)
            if playground.bbox(bomb4)[2] > 1280 or playground.bbox(bomb4)[0] < 0 or playground.bbox(bomb4)[1] < 0 or playground.bbox(bomb4)[2] > 720:
                Randombomb4()
                continuousmovebomb4()
            else:
                playground.after(80,continuousmovebomb4)
    def continuousmovebomb5():
        if running:
            playground.move(bomb5, 3, 5)
            if playground.bbox(bomb5)[2] > 1280 or playground.bbox(bomb5)[0] < 0 or playground.bbox(bomb5)[1] < 0 or playground.bbox(bomb5)[2] > 720:
                Randombomb5()
                continuousmovebomb5()
            else:
                playground.after(50,continuousmovebomb5)
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
        global running, score, scoreLabel, collide, playername, nameinput, reader, resetscore, resetcollide, GET1000FORFREE, KJ
        running = True
        pauseButton = Button(playground, image=pauseImg, bg="#ae7046", height=70, width=70, command=pause)
        pauseButton.place(x=500, y=20)
        #wake up the keyboard so they can be used once we press start
        keyboard()
        playButton.destroy()
        continuousmoveheart()
        continuousmoveicegold()
        continuousmoveshield()
        continuousmoveknife()
        continuousmovegoldblock()
        continuousmovegoldbox()
        if Allbombsoff is False and Fullbombs is True:
            continuousmovebomb()
            continuousmovebomb1()
            continuousmovebomb2()
            continuousmovebomb3()
            continuousmovebomb4()
            continuousmovebomb5()
        elif Allbombsoff is False and Fullbombs is False:
            continuousmovebomb3()
            continuousmovebomb4()
            continuousmovebomb5()
        playername = nameinput.get() #Like saving the name
        name = Label(playground, text=playername, font="Arial 20", fg="white", bg="#ae7046")
        name.place(x=100, y=30, anchor="center")
        with open('player.csv', 'r') as csvfile:
            fieldnames = ['Player', 'Score']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for line in reader:
                if line["Player"] == playername:
                    if int(line["Score"])<0:
                       resetscore = True
                    else:
                        resetscore = False
                    if resetscore is True:
                        if GET1000FORFREE is True and KJ is True:
                            score = 10000001000
                        elif GET1000FORFREE is True and KJ is False:
                            score = 1000
                        elif GET1000FORFREE is False and KJ is True:
                            score = 10000001000
                        else:
                            score = 0
                    else:
                        if GET1000FORFREE is True and KJ is False:
                            score = int(line["Score"]) + 1000
                        elif KJ is True and GET1000FORFREE is False:
                            score = int(line["Score"]) + 10000000000
                        elif KJ is False and GET1000FORFREE is False:
                            score = int(line["Score"])
                        elif KJ is True and GET1000FORFREE is True:
                            score = int(line["Score"]) + 10000001000
                    break
                else:
                    if GET1000FORFREE is True and KJ is False:
                        score = 1000
                    elif KJ is True and GET1000FORFREE is False:
                        score = 10000000000
                    elif KJ is True and GET1000FORFREE is True:
                        score = 10000001000
                    else:
                        score = 0



            scoreLabel = Label(playground, text="Score: " + str(score), font="Broadway 24", bg="#ae7046",fg="black")
            scoreLabel.place(x=620, y=20)
        if resetcollide is True:
            collide = 0
    #boundary boxes
    def hunterReachEdge():
        global hunterboundary
        hunterboundary = playground.bbox(hunter) #bbox is the boundary box
        if hunterboundary[0]<0:
            playground.move(hunter,20,0)
        elif hunterboundary[2]>1280:
            playground.move(hunter, -20, 0)
        elif hunterboundary[1]<50:
            playground.move(hunter, 0, 20)
        elif hunterboundary[3]>720:
            playground.move(hunter, 0, -20)
    #Collision detection(if collide, gain score, lose score or even gameover)
    def collideobjects():
        global score, collide
        HB = playground.bbox(heart)
        SL = playground.bbox(shield)
        KN = playground.bbox(knife)
        GBL = playground.bbox(goldblock)
        GBX = playground.bbox(goldbox)
        IG = playground.bbox(icegold)
        if Allbombsoff is False and Fullbombs is True:
            BB = playground.bbox(bomb)
            BB1 = playground.bbox(bomb1)
            BB2 = playground.bbox(bomb2)
            BB3 = playground.bbox(bomb3)
            BB4 = playground.bbox(bomb4)
            BB5 = playground.bbox(bomb5)
        elif Allbombsoff is False and Fullbombs is False:
            BB3 = playground.bbox(bomb3)
            BB4 = playground.bbox(bomb4)
            BB5 = playground.bbox(bomb5)
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
            scoreLabel.config(text="Score: "+str(score),fg="#E86411")
        elif hunterboundary[0] < SL[0] < hunterboundary[2] and hunterboundary[1]<SL[1]<hunterboundary[3]:#右下角
            Randomshield()
            score += 15
            scoreLabel.config(text="Score: " + str(score), fg="#E86411")
        elif hunterboundary[0] < SL[2] < hunterboundary[2] and hunterboundary[1] < SL[3] < hunterboundary[3]:#左上角
            Randomshield()
            score += 15
            scoreLabel.config(text="Score: " + str(score), fg="#E86411")
        elif hunterboundary[0] < SL[0] < hunterboundary[2] and hunterboundary[1]<SL[3]<hunterboundary[3]:#右上角
            Randomshield()
            score += 15
            scoreLabel.config(text="Score: " + str(score), fg="#E86411")
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
        if Allbombsoff is False and Fullbombs is True:
            if collide < 8 and score >=0:
                if hunterboundary[0]<BB[2]<hunterboundary[2] and hunterboundary[1]<BB[1]<hunterboundary[3]: #左下角
                    Randombomb()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: "+str(score), fg="#ff1100")
                elif hunterboundary[0] < BB[0] < hunterboundary[2] and hunterboundary[1]<BB[1]<hunterboundary[3]:#右下角
                    Randombomb()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB[2] < hunterboundary[2] and hunterboundary[1] < BB[3] < hunterboundary[3]:#左上角
                    Randombomb()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB[0] < hunterboundary[2] and hunterboundary[1]<BB[3]<hunterboundary[3]:#右上角
                    Randombomb()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                if hunterboundary[0]<BB1[2]<hunterboundary[2] and hunterboundary[1]<BB1[1]<hunterboundary[3]: #左下角
                    Randombomb1()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: "+str(score), fg="#ff1100")
                elif hunterboundary[0] < BB1[0] < hunterboundary[2] and hunterboundary[1]<BB1[1]<hunterboundary[3]:#右下角
                    Randombomb1()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB1[2] < hunterboundary[2] and hunterboundary[1] < BB1[3] < hunterboundary[3]:#左上角
                    Randombomb1()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB1[0] < hunterboundary[2] and hunterboundary[1]<BB1[3]<hunterboundary[3]:#右上角
                    Randombomb1()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                if hunterboundary[0]<BB2[2]<hunterboundary[2] and hunterboundary[1]<BB2[1]<hunterboundary[3]: #左下角
                    Randombomb2()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: "+str(score), fg="#ff1100")
                elif hunterboundary[0] < BB2[0] < hunterboundary[2] and hunterboundary[1]<BB2[1]<hunterboundary[3]:#右下角
                    Randombomb2()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB2[2] < hunterboundary[2] and hunterboundary[1] < BB2[3] < hunterboundary[3]:#左上角
                    Randombomb2()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB2[0] < hunterboundary[2] and hunterboundary[1]<BB2[3]<hunterboundary[3]:#右上角
                    Randombomb2()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                if hunterboundary[0]<BB3[2]<hunterboundary[2] and hunterboundary[1]<BB3[1]<hunterboundary[3]: #左下角
                    Randombomb3()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: "+str(score), fg="#ff1100")
                elif hunterboundary[0] < BB3[0] < hunterboundary[2] and hunterboundary[1]<BB3[1]<hunterboundary[3]:#右下角
                    Randombomb3()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB3[2] < hunterboundary[2] and hunterboundary[1] < BB3[3] < hunterboundary[3]:#左上角
                    Randombomb3()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB3[0] < hunterboundary[2] and hunterboundary[1]<BB3[3]<hunterboundary[3]:#右上角
                    Randombomb3()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                if hunterboundary[0]<BB4[2]<hunterboundary[2] and hunterboundary[1]<BB4[1]<hunterboundary[3]: #左下角
                    Randombomb4()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: "+str(score), fg="#ff1100")
                elif hunterboundary[0] < BB4[0] < hunterboundary[2] and hunterboundary[1]<BB4[1]<hunterboundary[3]:#右下角
                    Randombomb4()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB4[2] < hunterboundary[2] and hunterboundary[1] < BB4[3] < hunterboundary[3]:#左上角
                    Randombomb4()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB4[0] < hunterboundary[2] and hunterboundary[1]<BB4[3]<hunterboundary[3]:#右上角
                    Randombomb4()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                if hunterboundary[0]<BB5[2]<hunterboundary[2] and hunterboundary[1]<BB5[1]<hunterboundary[3]: #左下角
                    Randombomb5()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: "+str(score), fg="#ff1100")
                elif hunterboundary[0] < BB5[0] < hunterboundary[2] and hunterboundary[1]<BB5[1]<hunterboundary[3]:#右下角
                    Randombomb5()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB5[2] < hunterboundary[2] and hunterboundary[1] < BB5[3] < hunterboundary[3]:#左上角
                    Randombomb5()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB5[0] < hunterboundary[2] and hunterboundary[1]<BB5[3]<hunterboundary[3]:#右上角
                    Randombomb5()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
            else:
                gameover()
        elif Allbombsoff is False and Fullbombs is False:
            if collide < 8 and score >=0:
                if hunterboundary[0] < BB3[2] < hunterboundary[2] and hunterboundary[1] < BB3[1] < hunterboundary[3]:  # 左下角
                    Randombomb3()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB3[0] < hunterboundary[2] and hunterboundary[1] < BB3[1] < hunterboundary[
                    3]:  # 右下角
                    Randombomb3()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB3[2] < hunterboundary[2] and hunterboundary[1] < BB3[3] < hunterboundary[
                    3]:  # 左上角
                    Randombomb3()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB3[0] < hunterboundary[2] and hunterboundary[1] < BB3[3] < hunterboundary[
                    3]:  # 右上角
                    Randombomb3()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                if hunterboundary[0] < BB4[2] < hunterboundary[2] and hunterboundary[1] < BB4[1] < hunterboundary[
                    3]:  # 左下角
                    Randombomb4()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB4[0] < hunterboundary[2] and hunterboundary[1] < BB4[1] < hunterboundary[
                    3]:  # 右下角
                    Randombomb4()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB4[2] < hunterboundary[2] and hunterboundary[1] < BB4[3] < hunterboundary[
                    3]:  # 左上角
                    Randombomb4()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB4[0] < hunterboundary[2] and hunterboundary[1] < BB4[3] < hunterboundary[
                    3]:  # 右上角
                    Randombomb4()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                if hunterboundary[0] < BB5[2] < hunterboundary[2] and hunterboundary[1] < BB5[1] < hunterboundary[
                    3]:  # 左下角
                    Randombomb5()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB5[0] < hunterboundary[2] and hunterboundary[1] < BB5[1] < hunterboundary[
                    3]:  # 右下角
                    Randombomb5()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB5[2] < hunterboundary[2] and hunterboundary[1] < BB5[3] < hunterboundary[
                    3]:  # 左上角
                    Randombomb5()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
                elif hunterboundary[0] < BB5[0] < hunterboundary[2] and hunterboundary[1] < BB5[3] < hunterboundary[
                    3]:  # 右上角
                    Randombomb5()
                    if collide == 1:
                        score -= 30
                    if collide == 2:
                        score -= 50
                    if collide == 3:
                        score -= 100
                    if collide == 4:
                        score -= 150
                    if collide == 5:
                        score -= 200
                    if collide == 6:
                        score -= 300
                    if collide == 7:
                        score -= 400
                    collide += 1
                    scoreLabel.config(text="Score: " + str(score), fg="#ff1100")
            else:
                gameover()
    # Move the hunter in directions（default keys)
    def moveright(event):
        if running:
            playground.move(hunter, 20, 0)  # move the truck 10 units to the right
            hunterReachEdge() #everytime we move the hunter we call this EdgeReach function
            collideobjects()
    def moveleft(event):
        if running:
            playground.move(hunter, -20, 0)  # move the truck 10 units to the left
            hunterReachEdge()
            collideobjects()
    def moveup(event):
        if running:
            playground.move(hunter, 0, -20)  # move up the truck 10 units
            hunterReachEdge()
            collideobjects()
    def movedown(event):
        if running:
            playground.move(hunter, 0, 20)  # move down the truck 10 units
            hunterReachEdge()
            collideobjects()



    # Keyboard Settings (Making the hunter move)
    def keyboard():
        playground.bind_all("<Up>", moveup)
        playground.bind_all("<w>", moveup)
        playground.bind_all("<Down>", movedown)
        playground.bind_all("<s>", movedown)
        playground.bind_all("<Right>", moveright)
        playground.bind_all("<d>", moveright)
        playground.bind_all("<Left>", moveleft)
        playground.bind_all("<a>", moveleft)

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
        homeButton = Button(pausescreen, text="Home", font="Algerian 20", fg="orange", bg="#ae7046", command=backtohome)
        homeButton.place(x=550, y=270)
        restartbutton = Button(pausescreen, image=restartImg, command=restartfrompause, bg="#ae7046", height=110, width=110)
        restartbutton.place(x=550, y=360)
        writenameandscore()
    #Resume the game
    def resume():
        global score, scoreLabel, resetscore, resetcollide
        resetscore = False
        resetcollide = False
        pausescreen.destroy()
        scoreLabel.destroy()
        startgame()
    #End the game( need to save score and playername)
    def backtohome(): #back to home
        global score, scoreLabel, resetscore,collide,nameinputscreen,GET1000FORFREE,KJ,Allbombsoff,Fullbombs
        GET1000FORFREE = False
        KJ = False
        Fullbombs = True
        Allbombsoff = False
        nameinputscreen.destroy()
        resetscore = True
        collide = 0
    #Gameover when collide with bomb
    def gameover():
        global running, backgroundImg, gameoverscreen,GET1000FORFREE, KJ, Fullbombs, Allbombsoff
        #save username and score
        running = False
        GET1000FORFREE = False
        KJ = False
        Fullbombs = True
        Allbombsoff = False
        gameoverscreen = Canvas(playground, width=1280, height=720)
        gameoverscreen.pack()
        backgroundImg = PhotoImage(file="bg1.png")
        bg = gameoverscreen.create_image(450, 450, image=backgroundImg)
        gameoverword = Label(gameoverscreen, text="Game Over!", font="Algerian 50", fg="red", bg="#ae7046")
        gameoverword.place(x=450, y=100)
        restartbutton = Button(gameoverscreen, image=restartImg, command = restartfromgameover, bg="#ae7046", height=110, width=110 )
        restartbutton.place(x=550, y=360)
        homeButton = Button(gameoverscreen, text="Home", font="Algerian 20", fg="orange", bg="#ae7046", command=backtohome)
        homeButton.place(x=550, y=270)
        writenameandscore()
    #Restart the game after game over
    def restartfromgameover():
        global score, scoreLabel, gameoverscreen, resetcollide,resetscore,GET1000FORFREE,KJ,Fullbombs,Allbombsoff
        gameoverscreen.destroy()
        scoreLabel.destroy()
        GET1000FORFREE = False
        KJ = False
        Fullbombs = True
        Allbombsoff = False
        resetscore = True
        resetcollide = True
        startgame()
    def restartfrompause():
        global score, scoreLabel, gameoverscreen, resetcollide, resetscore
        pausescreen.destroy()
        scoreLabel.destroy()
        resetscore = True
        resetcollide = True
        startgame()

    def writenameandscore():
        global score, playername, nameinput
        print(playername)
        fieldnames = ['Player', 'Score']
        with open('player.csv', 'r',newline="") as csvfile:
            fieldnames = ['Player', 'Score']
            reader = csv.reader(csvfile)
            playerlist = list(reader)
            for i in range(1,len(playerlist)):
                if playerlist[i] =='':
                    del playerlist[i]
                elif playerlist[i][0] == playername: #overwrite playername
                    playerlist[i][1] = score
                    with open('player.csv','w',newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(playerlist)
                    break
            else:
                with open('player.csv', 'a',newline='') as csvfile:
                    fieldnames = ['Player', 'Score']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'Player': playername, 'Score': score})


        csvfile.close()



    #buttons
    playButton = Button(playground, text="Play", font="Algerian 20", fg="orange", bg="#ae7046", command = startgame)
    playButton.place(x=50,y=10)
    bossbutton = Button(playground, text="Boss", command=bossmode, bg="#ae7046")
    bossbutton.place(x=50, y=100)
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
    infoButton = Button(menu, image=infoImg, command=infoscreen, bg="#ae7046", height=110, width=110)
    infoButton.place(x=300, y=400)
    bossbutton = Button(menu, text="Boss", command=bossmode,bg="#ae7046")
    bossbutton.place(x=50, y=600)



    menu.mainloop()

#leadershipboardscreen
def leaderboardtohome():
    global mainframe
    mainframe.destroy()

def leaderboardscreen():
    global menu, leaderboard, backgroundImg, mainframe
    # create frame and scroll bar
    mainframe = Frame(menu)
    mainframe.pack(fill=BOTH, expand=1)
    leaderboard = Canvas(mainframe, width=1260, height =720, bg="#E86411")
    leaderboard.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=leaderboard.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    # Titile
    slogan = Label(leaderboard, text="Leadership Board", font="Algerian 48", fg="black", bg="#E86411")
    slogan.place(x=640, y=45, anchor="center")
    # backgroundImg = PhotoImage(file="bg1.png")
    # leaderboard.create_image(350, 450, image=backgroundImg)
    #configure the canvas
    leaderboard.configure(yscrollcommand=scrollbar.set)
    leaderboard.bind('<Configure>', lambda e: leaderboard.configure(scrollregion = leaderboard.bbox("all")))
    #create second frome
    secondframe = Frame(leaderboard)
    leaderboard.create_window((0,0), window = secondframe, anchor="nw")
    y_axis = 100
    with open('player.csv', 'r', newline='') as f:
         reader = csv.reader(f, delimiter=',')
         header = next(reader)
         rows = [header] + [[row[0], int(row[1])] for row in reader if row]
         rows[1:] = sorted(rows[1:], key=lambda x: x[1], reverse=True)

    with open('player.csv', 'w', newline="") as csvfile:
           writer = csv.writer(csvfile)
           writer.writerows(rows)
    with open('player.csv', 'r',newline="") as csvfile:
         fieldnames = ["Player", "Score"]
         reader = csv.DictReader(csvfile, fieldnames=fieldnames)
         for line in reader:
              leaderboard.create_text(450,y_axis, text=line["Player"], font="Broadway 24")
              leaderboard.create_text(700,y_axis, text=line["Score"], font="Broadway 24")
              y_axis+=60
    points =[100,10,40,198,190,78,10,78,160,198]
    leaderboard.create_polygon(points,outline ="orange", fill="orange")

    #make button
    menuButton = Button(leaderboard, text="Home", font="Algerian 20", fg="orange", bg="#E86411", command=leaderboardtohome)
    menuButton.place(x=200, y=270)

# boss key
def bossmode():
    global running
    running = False
    url = 'http://www.bbcnews.com'
    webbrowser.open_new(url)





#cheat screen
def exitcheatscreen():
    cheat.destroy() #return to home page
def checkcheatcode():
    global score, cheatcodeinput,Fullbombs,GET1000FORFREE,KJ,Allbombsoff
    cheatcode = cheatcodeinput.get()
    if cheatcode == "GETTHE1000FORFREE":
        GET1000FORFREE = True
        #score +=1000(written in startgame)
        messagebox.showinfo("Popup","Cheatcode applied!")
        cheat.destroy()
    elif cheatcode == "KJ":
        KJ = True
        #score +=1000(written in startgame)
        messagebox.showinfo("Popup","Cheatcode applied!")
        cheat.destroy()

    elif cheatcode =="REDUCESOMEBOMBS":
        Fullbombs = False
        messagebox.showinfo("Popup","Cheatcode applied!")
        cheat.destroy()
    elif cheatcode == "IAMTHEGOD":
        Allbombsoff = True
        messagebox.showinfo("Popup","Cheatcode applied!")
        cheat.destroy()
    else:
        messagebox.showwarning("Popup","Failed!")
def cheatscreen():
    global cheat, backgroundImg,cheatcodeinput
    cheat = Canvas(menu, width=1280, height =720)
    cheat.pack()

    # Titile
    title = Label(cheat, text="Are U ready cheating?", font="Algerian 24", fg="black", bg="#ae7046")
    title.place(x=640, y=30, anchor="center")
    # background
    backgroundImg = PhotoImage(file="bg1.png")
    bg = cheat.create_image(450, 450, image=backgroundImg)
    # input box
    cheatcodeinput = Entry(cheat)
    cheatcodeinput.configure(bg="#ae7046", fg="black", font="Arial 24")
    cheat.create_window(600, 200, window=cheatcodeinput, height=40, width=800)
    applycheatcodeButton = Button(cheat, text="Apply", font="Algerian 24", fg="black", bg="#ae7046",
                             command=checkcheatcode)  # click startbutton to call the gamescreen  function
    applycheatcodeButton.place(x=500, y=400)
    exitButton = Button(cheat, text="Cancel&Exit", font="Algerian 24", fg="black", bg="#ae7046", command=exitcheatscreen)
    exitButton.place(x=500, y=300)

#playernameinput
def inputtohome():
    global nameinputscreen
    nameinputscreen.destroy()
def playerinputscreen():
    global nameinputscreen, backgroundImg, nameinput
    nameinputscreen = Canvas(menu, width=1280, height=720)
    nameinputscreen.pack()
    # Titile
    title = Label(nameinputscreen, text="Please enter player name", font="Algerian 24", fg="black", bg="#ae7046")
    title.place(x=640, y=30, anchor="center")
    # background
    backgroundImg = PhotoImage(file="bg1.png")
    bg = nameinputscreen.create_image(450, 450, image=backgroundImg)
    #input box
    nameinput = Entry(nameinputscreen)
    nameinput.configure(bg="#ae7046", fg="black", font="Arial 24")
    nameinputscreen.create_window(600, 200, window=nameinput, height=40, width=800)
    startgameButton = Button(nameinputscreen, text="Save&Start", font="Algerian 24", fg="black", bg="#ae7046", command=gamescreen)  # click startbutton to call the gamescreen  function
    startgameButton.place(x=500, y=400)
    menuButton = Button(nameinputscreen, text="Home", font="Algerian 24", fg="black", bg="#ae7046",command=inputtohome)
    menuButton.place(x=500, y=300)

def exitinfoscreen():
    info.destroy()
def infoscreen():
    global info, backgroundImg
    info = Canvas(menu, width=1280, height =720, bg="black")
    info.pack()

    # Titile
    title = Label(info, text="Introduction", font="Arial 24", fg="White", bg="black")
    title.place(x=640, y=50, anchor="center")
    text="Treasure Hunter is a newly design game that requires 100% concrentration from players.\n You are aiming to collect different kinds of treasures to get the highest score possible, while you need to prevent hitting the bomb \n as you will lose 100 points for the first time then the next time you will lose an extra 100. If you hit the bomb 5 times, you lose.\nThere are cheatcodes that you can apply, as long as you guess the correct ones. Enjoy the game.\n GodofGame Inc. "

    intro = Label(info, text=text, font="Arial 15", fg="White", bg="black")
    intro.place(x=640, y=200, anchor="center")
    exitButton = Button(info, text="Exit", font="Arial 10", fg="white", bg="black",
                        command=exitinfoscreen)
    exitButton.place(x=600, y=600)





startscreen()


