from tkinter import *
import random
import Robot

master = Tk()
#can change width*height
width_height=500
w = Canvas(master, 
           width=width_height,
           height=width_height,bg='white')
w.pack()
#Black
B1=random.random()*(width_height-50)
w.create_rectangle(B1, B1, B1+50, B1+50, fill='Black')
B2=random.random()*(width_height-50)
w.create_rectangle(B2, B2, B2+50, B2+50, fill='Black')
B3=random.random()*(width_height-50)
w.create_rectangle(B3, B3, B3+50, B3+50, fill='Black')
G1=random.random()*(width_height-50)
#GRAY
w.create_rectangle(G1, G1, G1+50, G1+50, fill='gray')
G2=random.random()*(width_height-50)
w.create_rectangle(G2, G2, G2+50, G2+50, fill='gray')
G3=random.random()*(width_height-50)
w.create_rectangle(G3, G3, G3+50, G3+50, fill='gray')

robot_sim=[]
for i in range(0,100):
    x=random.random()*(width_height-10)+10
    y=random.random()*(width_height-10)+10
    #CHECK IF BLACK
    while((x>=B1 and x<=B1+50 and y>=B1 and y<=B1+50) or 
          (x>=B2 and x<=B2+50 and y>=B2 and y<=B2+50) or
          (x>=B3 and x<=B3+50 and y>=B3 and y<=B3+50)):
        x=random.random()*width_height
        y=random.random()*width_height
    w.create_oval(x, y, x+10, y+10, fill='red')
    w.create_text(x, y-6, text=i)
mainloop()