import tkinter
import PIL.Image
import PIL.ImageTk
import random

root = tkinter.Tk()

l = 10
def remained_life():

    global l
    Life.set(l)
    if l > 0:
        new_time = Life.get() - 1
        Life.set(new_time)
        l -= 1
        root.after(1000, remained_life)

    else :
        print(f"You lived {time} seconds.")
        quit()


time=0
def passed_time():

    global time
    if time < 1000:
        new_time = pstime.get() + 1
        pstime.set(new_time)
        root.after(1000, passed_time)
        time += 1


def move_kitty(event):

    if event.keysym == 'Up':
        mainCanvas.move(labelk, 0, -8)
    elif event.keysym == 'Down':
        mainCanvas.move(labelk, 0, 8)


def resize(up):

    global photok  # Always keep a reference to PhotoImage (it clears the photos with garbage collector)
    if up:
        x = int(photok.width()*5/4)
        y = int(photok.height()*5/4)
        imgk = PIL.Image.open("img/kittyy.png").resize((x,y))
        photok = PIL.ImageTk.PhotoImage(imgk)
        mainCanvas.itemconfig(labelk, image=photok)
        ck = mainCanvas.coords(labelk)
        mainCanvas.coords(labelk, ck[0], ck[1])

    elif not up:
        x = int(photok.width()*3/4)
        y = int(photok.height()*3/4)
        imgk = PIL.Image.open("img/kittyy.png").resize((x,y))
        photok = PIL.ImageTk.PhotoImage(imgk)
        mainCanvas.itemconfig(labelk, image=photok)
        ck = mainCanvas.coords(labelk)
        mainCanvas.coords(labelk, ck[0], ck[1])


countu = 0
def up_arrow():

    global photok, photou, countu
    cu = mainCanvas.coords(labelu)
    ck = mainCanvas.coords(labelk)

    if  (cu[0] in range(int(photok.width())) or cu[0]+photou.width() in range(int(photok.width()))) and countu == 0 \
            and (cu[1] in range(int(ck[1]),int(ck[1] + photok.height())) or cu[1]+photou.height() in range(int(ck[1]),int(ck[1] + photok.height()))
            or cu[1]+photou.height()/2 in range(int(ck[1]),int(ck[1] + photok.height()))):
        resize(up=True)
        countu += 1


def up_arrow_place():

    global randu, photou, countu
    chc = [3000,4000,5000]
    randu = random.choice(chc)
    mainCanvas.itemconfig(labelu, image=photou)
    mainCanvas.coords(labelu, 1150, random.randint(0,550))
    countu = 0
    root.after(randu,up_arrow_place)


countd=0
def down_arrow():

    global photok,photod, countd
    ck = mainCanvas.coords(labelk)
    cd = mainCanvas.coords(labeld)

    if  (cd[0] in range(int(photok.width())) or cd[0]+photod.width() in range(int(photok.width()))) and countd==0\
            and (cd[1] in range(int(ck[1]),int(ck[1] + photok.height())) or cd[1]+photod.height() in range(int(ck[1]),int(ck[1] + photok.height())) \
            or cd[1]+photod.height()/2 in range(int(ck[1]),int(ck[1] + photok.height()))):
        resize(up=False)
        countd += 1


def down_arrow_place():

    global randd, photod, countd
    chc = [3000,4000,5000]
    randd = random.choice(chc)
    mainCanvas.itemconfig(labeld, image=photod)
    mainCanvas.coords(labeld, 1150, random.randint(0,550))
    countd = 0
    root.after(randd, down_arrow_place)


def skull():

    global l, photos
    ck = mainCanvas.coords(labelk)
    cs = mainCanvas.coords(labels)

    if  (cs[0] in range(int(photok.width())) or cs[0]+photos.width() in range(int(photok.width()))) \
            and (cs[1] in range(int(ck[1]),int(ck[1] + photok.height())) or cs[1]+photos.height() in range(int(ck[1]),int(ck[1] + photok.height()))
            or cs[1]+photos.height()/2 in range(int(ck[1]),int(ck[1] + photok.height()))):
        l=0


def skull_place():

    global rands, photos
    chc = [3000,4000,5000]
    rands = random.choice(chc)
    mainCanvas.itemconfig(labels, image=photos)
    mainCanvas.coords(labels, 1150, random.randint(0,550))
    root.after(rands, skull_place)


def skull2():

    global l, photos2
    ck = mainCanvas.coords(labelk)
    cs = mainCanvas.coords(labels2)

    if  (cs[0] in range(int(photok.width())) or cs[0]+photos2.width() in range(int(photok.width()))) \
            and (cs[1] in range(int(ck[1]),int(ck[1] + photok.height())) or cs[1]+photos2.height() in range(int(ck[1]),int(ck[1] + photok.height()))
                 or cs[1]+photos2.height()/2 in range(int(ck[1]),int(ck[1] + photok.height()))):
        l=0


def skull_place2():

    global rands2, photos2
    chc = [3000,4000,5000]
    rands2 = random.choice(chc)
    mainCanvas.itemconfig(labels2, image=photos2)
    mainCanvas.coords(labels2, 1150, random.randint(0,550))
    root.after(rands2, skull_place2)


def ball_choose(num):

    ballstr = f"img/ball{num}.jpg"
    imgbal = PIL.Image.open(ballstr).resize((int(200/num), int(200/num)))
    return imgbal


countb = 0
def ball_call(n):

    global ballnum, photoball, photok, l, countb
    ballnum = n
    photoball = PIL.ImageTk.PhotoImage(ball_choose(ballnum))
    mainCanvas.itemconfig(labelball, image=photoball)
    ck = mainCanvas.coords(labelk)
    cb = mainCanvas.coords(labelball)

    if  (cb[0] in range(int(photok.width())) or cb[0]+photoball.width() in range(int(photok.width()))) and countb==0 \
            and (cb[1] in range(int(ck[1]),int(ck[1] + photok.height())) or cb[1]+photoball.height() in range(int(ck[1]),int(ck[1] + photok.height()))
            or cb[1]+photoball.height()/2 in range(int(ck[1]),int(ck[1] + photok.height())) or ck[1]+photok.height()/2 in range(int(cb[1]),int(cb[1] + photoball.height()))):
        l += n*photok.width()/50
        countb+=1


def ball_place():

    global randb, randBallNum, photoball, countb
    chc = [3000,4000,5000]
    randb = random.choice(chc)
    mainCanvas.itemconfig(labelball, image=photoball)
    mainCanvas.coords(labelball, 1150, random.randint(0,550))
    balllist = [1,3,4,5,6,10]
    randBallNum = random.choice(balllist)
    countb = 0
    root.after(randb, ball_place)


def slide_images():

    global randu, randd, rands, rands2, randb, randBallNum
    mainCanvas.move(labelu, -150000/randu, 0)
    mainCanvas.move(labeld, -150000/randd, 0)
    mainCanvas.move(labels, -150000/rands, 0)
    mainCanvas.move(labels2, -150000/rands2, 0)
    mainCanvas.move(labelball, -150000/randb, 0)
    up_arrow()
    down_arrow()
    skull()
    skull2()
    ball_call(randBallNum)
    root.after(80, slide_images)


root.title("Run kitty run!")
root.geometry("1280x720")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=20)
root.rowconfigure(1, weight=1)

mainCanvas = tkinter.Canvas(root, relief="sunken", borderwidth=4, background="white")
mainCanvas.grid(row=0, column=0, sticky='ewns')

mainCanvas.columnconfigure(0, weight=1)
mainCanvas.columnconfigure(1, weight=1)
mainCanvas.columnconfigure(2, weight=1)
mainCanvas.columnconfigure(3, weight=1)
mainCanvas.columnconfigure(4, weight=1)
mainCanvas.columnconfigure(5, weight=1)

imgk = PIL.Image.open("img/kittyy.png").resize((150, 120))
photok = PIL.ImageTk.PhotoImage(imgk)
labelk = mainCanvas.create_image(10, 10, anchor=tkinter.NW, image=photok)

ballnum = 1
photoball = PIL.ImageTk.PhotoImage(ball_choose(ballnum))
labelball = mainCanvas.create_image(500, 200, anchor=tkinter.NW, image=photoball)

imgu = PIL.Image.open("img/uparrow.png").resize((100, 80))
photou = PIL.ImageTk.PhotoImage(imgu)
labelu = mainCanvas.create_image(1000, 10, anchor=tkinter.NW, image=photou)

imgd = PIL.Image.open("img/downarrow.png").resize((100, 80))
photod = PIL.ImageTk.PhotoImage(imgd)
labeld = mainCanvas.create_image(1000, 300, anchor=tkinter.NW, image=photod)

imgs = PIL.Image.open("img/skull.png").resize((150, 120))
photos = PIL.ImageTk.PhotoImage(imgs)
labels = mainCanvas.create_image(1150, 550, anchor=tkinter.NW, image=photos)

imgs2 = PIL.Image.open("img/skull.png").resize((170, 150))
photos2 = PIL.ImageTk.PhotoImage(imgs2)
labels2 = mainCanvas.create_image(1150, 550, anchor=tkinter.NW, image=photos2)

textCanvas = tkinter.Canvas(root, relief="sunken", borderwidth=4, background="white")
textCanvas.grid(row=1, column=0, columnspan=2, sticky='ewns')
textCanvas.columnconfigure(0, weight=1)
textCanvas.columnconfigure(1, weight=1)
textCanvas.columnconfigure(2, weight=300)
textCanvas.columnconfigure(3, weight=1)

Life = tkinter.IntVar()
Life.set(10)
tkinter.Label(textCanvas, text="Remaining Life: ", background="white").grid(row=0, column=0, sticky="w")
tkinter.Label(textCanvas, textvariable=Life, background="white").grid(row=0, column=1, sticky="w")

pstime = tkinter.IntVar()
pstime.set(0)
tkinter.Label(textCanvas, text="Passing Time: ", background="white").grid(row=0, column=2, sticky="e")
tkinter.Label(textCanvas, textvariable=pstime, background="white").grid(row=0, column=3)

passed_time()
remained_life()
up_arrow_place()
down_arrow_place()
skull_place()
skull_place2()
ball_place()
slide_images()

root.bind("<KeyPress-Up>", move_kitty)
root.bind("<KeyPress-Down>", move_kitty)

root.mainloop()
