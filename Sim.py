from tkinter import *
import random
import Robot
import math

def checkered(w, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,width_height,line_distance):
      w.create_line(x, 0, x, width_height, fill='Black')
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,width_height,line_distance):
      w.create_line(0, y, width_height, y, fill='Black')       


master = Tk()
#can change width*height
width_height=500
w = Canvas(master, 
           width=width_height,
           height=width_height,bg='white')
w.pack()
#Black
B1=random.random()*50
w.create_rectangle(B1, B1, B1+50, B1+50, fill='Black')
B2=random.randint(200,250)
w.create_rectangle(B2, B2, B2+50, B2+50, fill='Black')
#GRAY
G1=random.randint(100,150)
w.create_rectangle(G1, G1, G1+50, G1+50, fill='gray')
G2=random.randint(300,350)
w.create_rectangle(G2, G2, G2+50, G2+50, fill='gray')


robot_sim=[]
for i in range(0,100):
    x=random.randint(10,width_height-10)
    y=random.randint(10,width_height-10)
    #CHECK IF BLACK
    while((x>=B1 and x<=B1+50 and y>=B1 and y<=B1+50) or 
          (x>=B2 and x<=B2+50 and y>=B2 and y<=B2+50)):
        x=random.randint(10,width_height-10)
        y=random.randint(10,width_height-10)
    #robot randon
    if(i==50):
        w.create_oval(x, y, x+10, y+10, fill='red')
        w.create_text(x, y-6, text=i, fill='green')
    else:
        w.create_oval(x, y, x+10, y+10, fill='green')
        w.create_text(x, y-6, text=i, fill='green')
    if((x>=G1 and x<=G1+50 and y>=G1 and y<=G1+50) or 
          (x>=G2 and x<=G2+50 and y>=G2 and y<=G2+50)):
            robot_sim.insert(i, Robot.Robot(x,y,'gray',i))
    else:
        robot_sim.insert(i, Robot.Robot(x,y,'white',i))
    
checkered(w,10)
min=10000

#check robot closest to robotID=50
for i in range(0,100):
    if(i!=50):
        dist=int(math.sqrt(math.pow(robot_sim[i].x-robot_sim[50].x,2)+math.pow(robot_sim[i].y-robot_sim[50].y,2)))
        if(dist<min):
            min=dist
            id=i

print("the robotID best closest is: ",id," dist: ",min)

#move Robots
for i in range(0,100):
    robot_sim[i].moveLeft(B1,B2)
    robot_sim[i].Battery()
    
for i in range(0,100):
    w.create_oval(robot_sim[i].x, robot_sim[i].y, robot_sim[i].x+10, robot_sim[i].y+10, fill='blue')
    w.create_text(robot_sim[i].x, robot_sim[i].y-6, text=i, fill='blue')


w.mainloop()



