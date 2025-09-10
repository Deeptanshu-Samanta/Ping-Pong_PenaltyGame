import tkinter as tk
import time
import random
from RESTART import replay 


def move_left(event):
    coordinates=canvas.coords(plank)
    if(coordinates[0]>0):
        canvas.move(plank,-20,0)

def move_right(event):
    coordinates=canvas.coords(plank)
    if(coordinates[2]<700):
        canvas.move(plank,20,0)

def reset_positions():
    """Reset ball and plank when a goal or miss happens"""
    canvas.coords(plank, 300, 475, 450, 500)   # reset plank
    canvas.coords(ball, 333, 10, 367, 45)      # reset ball
    window.update()
    time.sleep(1)  

def score_card(score):
    canvas.itemconfig(score_label,text=f"Score: {score}")
    
def restart_game(label2=None, button_replay=None):
    global score, outs, score_label, plank, ball, goal
    if button_replay:   
        button_replay.destroy()
    if label2:
        canvas.delete(label2)

    score = 0
    outs = 0

    # Reset canvas
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_obj, anchor='nw')
    plank = canvas.create_rectangle(300, 475, 400, 500, fill='#99EDC3', outline='#3DED97', width='4')
    ball = canvas.create_oval(333, 10, 367, 45, fill='#960018', outline='#FF2400', width='3')
    goal = canvas.create_rectangle(250, 0, 450, 20, fill='#777B7E', outline='#3E424B', width='5')

    # Recreate score text
    score_label = canvas.create_text(350, 200, text="Score: 0", font=("Times New Roman", 30), fill='brown', tag="score")

    # Start game again
    ball_movement()


#moving the ball
#ball_movement()
def ball_movement():
    global outs,score
    button.destroy()

    xVelocity,yVelocity=random.choice([-1,1]),1
    while True:
        coordinates=canvas.coords(ball)
        coord=canvas.coords(plank)
        if(coordinates[0]<0 or coordinates[0]>=w-50):
            xVelocity=-xVelocity
        if (coordinates[1]<0 and coordinates[0]>250 and coordinates[0]<450-35):
            score+=1
            score_card(score)
            reset_positions()
            time.sleep(1)
            return ball_movement()
        if(coordinates[1]<0):
            yVelocity=-yVelocity
        if ((coord[0]<coordinates[0]<coord[2] or coord[0]<coordinates[2]<coord[2]) and coord[1]-30<coordinates[1]<coord[3]-30):
            yVelocity=-yVelocity

        if(coordinates[1]>500):
            if outs<0:
                outs+=1
                reset_positions()
                return ball_movement()
                
            else:
                canvas.delete(score_label)
                time.sleep(1)
                #print("SCORE is", score)
                #score_label.destroy()
                replay(canvas,window,score,restart_game)
                
                window.update()
            
        canvas.move(ball,xVelocity,yVelocity)
        window.update()
        time.sleep(0.005)

window=tk.Tk()

#creating base window

h,w=500,700
canvas=tk.Canvas(window,width=w,height=h)
canvas.pack()

# adding background image and object image
bg_obj=tk.PhotoImage(file='C:\\Users\\deept\\OneDrive\\Desktop\\game1\\pure-black-background.jpg')
bg=canvas.create_image(0,0,image=bg_obj,anchor='nw')

plank=canvas.create_rectangle(300,475,400,500,fill='#99EDC3',outline='#3DED97',width='4')
ball=canvas.create_oval(333,10,367,45,fill='#960018', outline='#FF2400',width='3')
goal=canvas.create_rectangle(250,0,450,20,fill='#777B7E',outline='#3E424B',width='5')

#moving the plank
window.bind('<Left>',move_left)
window.bind('<Right>',move_right)

outs=score=0
score_label=canvas.create_text(350,200, text="Score:"+str(score), font=("Times New Roman",30),fill='brown')


button=tk.Button(window, text="PLAY!!", command=ball_movement ,font=("Arial",25),fg="black",bg="white",)
button.place(relx=0.4, rely=0.65)

window.mainloop()

