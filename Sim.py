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
#GRAY
G1=random.random()*(width_height-50)
w.create_rectangle(G1, G1, G1+50, G1+50, fill='gray')
G2=random.random()*(width_height-50)
w.create_rectangle(G2, G2, G2+50, G2+50, fill='gray')
G3=random.random()*(width_height-50)
w.create_rectangle(G3, G3, G3+50, G3+50, fill='gray')

def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,width_height,line_distance):
      canvas.create_line(x, 0, x, width_height, fill='Black')
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,width_height,line_distance):
      canvas.create_line(0, y, width_height, y, fill='Black')

robot_sim=[]
for i in range(0,100):
    x=random.random()*(width_height-10)
    y=random.random()*(width_height-10)
    #CHECK IF BLACK
    while((x>=B1 and x<=B1+50 and y>=B1 and y<=B1+50) or 
          (x>=B2 and x<=B2+50 and y>=B2 and y<=B2+50) or
          (x>=B3 and x<=B3+50 and y>=B3 and y<=B3+50)):
        x=random.random()*(width_height-10)
        y=random.random()*(width_height-10)
    w.create_oval(x, y, x+10, y+10, fill='green')
    w.create_text(x, y-6, text=i, fill='green')
checkered(w,10)
mainloop()
