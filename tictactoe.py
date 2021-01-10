from tkinter import *
from tkinter import messagebox
import random

def restartProgram():
    global moves
    global places
    global playermoves
    global pcmoves
    places = ["1","2","3","4","5","6","7","8","9"]
    pcmoves = []
    playermoves = []
    moves = 0
    c.delete(ALL)
    c.create_line(100,0,100,300)
    c.create_line(200,0,200,300)
    c.create_line(300,0,300,300)
    c.create_line(0,100,300,100)
    c.create_line(0,200,300,200)
    c.create_line(0,300,300,300)

def leftClick(event):
    global moves
    global places
    global playermoves
    if not(moves == 9 or checkWin(pcmoves) or checkWin(playermoves)):
        placex = event.x // 100 % 3 + 1
        placey = event.y // 100 % 3 + 1
        px = (placex - 1) % 3 * 100 + 51
        py = (placey - 1) % 3 * 100 + 51
        if placex == 1:
            if placey == 1:
                place = 1
            elif placey == 2:
                place = 4
            else:
                place = 7
        elif placex == 2:
            if placey == 1:
                place = 2
            elif placey == 2:
                place = 5
            else:
                place = 8
        else:
            if placey == 1:
                place = 3
            elif placey == 2:
                place = 6
            else:
                place = 9
        if str(place) in places:
            c.create_image(px,py,image=x)
            places.remove(str(place))
            playermoves.append(str(place))
            moves += 1
            if checkWin(playermoves) == False:
                pcTurn()
            else:
                messagebox.showinfo("Console","You win!")
        c.update()
    else:
        restartProgram()

def rightClick(event):
    pcTurn()
    
def pcTurn():
    global places
    global moves
    move = 0
    if not(moves >= 9):
        for count in range(1,10):
            if str(count) in places:
                pcmoves.append(str(count))
                if checkWin(pcmoves):
                    move = count
                pcmoves.remove(str(count))
        if move == 0:
            for count in range(1,10):
                if str(count) in places:
                    playermoves.append(str(count))
                    if checkWin(playermoves):
                        move = count
                    playermoves.remove(str(count))
        if move == 0:
            move = random.randint(1,9)
            while str(move) not in places:
                move = random.randint(1,9)
        px = ((int(move)-1) % 3) * 100 + 51
        py = ((int(move)-1) // 3) * 100 + 51
        c.create_image(px,py,image=o)
        pcmoves.append(str(move))
        places.remove(str(move))
        moves += 1
        if checkWin(pcmoves):
            messagebox.showinfo("Console","The pc has won!")
        elif moves == 9:
            messagebox.showinfo("Console","It is a tie")
    else:
        messagebox.showinfo("Console","It is a tie")
    c.update()

def checkWin(moves):
    if set(["1","2","3"]) <= set(moves):
        return True
    elif set(["4","5","6"]) <= set(moves):
        return True
    elif set(["7","8","9"]) <= set(moves):
        return True
    elif set(["1","4","7"]) <= set(moves):
        return True
    elif set(["2","5","8"]) <= set(moves):
        return True
    elif set(["3","6","9"]) <= set(moves):
        return True
    elif set(["1","5","9"]) <= set(moves):
        return True
    elif set(["3","5","7"]) <= set(moves):
        return True
    else:
        return False

root = Tk()
root.title("Tic Tac Toe")
root.minsize(300,300)
root.maxsize(300,300)
c = Canvas(root,width=300,height=300)
c.place(x=0,y=0)
c.focus_set()

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Restart",command=restartProgram)
filemenu.add_separator()
filemenu.add_command(label="PC Move",command=lambda:pcTurn())
menubar.add_cascade(label="File",menu = filemenu)

root.config(menu=menubar)

c.create_line(100,0,100,300)
c.create_line(200,0,200,300)
c.create_line(300,0,300,300)
c.create_line(0,100,300,100)
c.create_line(0,200,300,200)
c.create_line(0,300,300,300)

x = PhotoImage(file="x.gif")
o = PhotoImage(file="o.gif")

places = ["1","2","3","4","5","6","7","8","9"]
pcmoves = []
playermoves = []
moves = 0

c.bind("<Button-1>",leftClick)
c.bind("<Button-3>",rightClick)
root.mainloop()
