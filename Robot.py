class Robot:
    def __init__(self,x,y,color,id):
        self.x=x
        self.y=y
        self.id=id
        self.battery=100
        self.color=color
        if(color=='gray'):
            print('RobotID:', id, ' in Zone Gray')
            
            
    def moveLeft(self,B1,B2):
        if(self.battery>9 and((self.x-10<B1 or self.x-10>B1+50) or (self.y<B1 or self.y>B1+50)) or ((self.x-5<B2 or self.x-5>B2+50) or (self.y<B2 or self.y>B2+50))):
            self.x=self.x-10
            self.battery=self.battery-10
        else:
            print("RobotID ",self.id,"cant move")
        
    def moveRight(self,B1,B2):
        if(self.battery>9 and((self.x+10<B1 or self.x+10>B1+50) or (self.y<B1 or self.y>B1+50)) or ((self.x+10<B2 or self.x+10>B2+50) or (self.y<B2 or self.y>B2+50))):
            self.x=self.x+10
            self.battery=self.battery-10
        else:
            print("RobotID ",self.id,"cant move")
            
    def moveUp(self,B1,B2):
        if(self.battery>9 and((self.x<B1 or self.x>B1+50) or (self.y+10<B1 or self.y+10>B1+50)) or ((self.x<B2 or self.x>B2+50) or (self.y+10<B2 or self.y+10>B2+50))):
            self.y=self.y+10
            self.battery=self.battery-10
        else:
            print("RobotID ",self.id,"cant move")
            
    def moveDown(self,B1,B2):
        if(self.battery>9 and((self.x<B1 or self.x>B1+50) or (self.y-10<B1 or self.y-10>B1+50)) or ((self.x<B2 or self.x>B2+50) or (self.y-10<B2 or self.y-5>B2+50))):
            self.y=self.y-10
            self.battery=self.battery-10
        else:
            print("RobotID ",self.id,"cant move")
            
    def Battery(self):
        if (self.battery < 100 and self.color=='white'):
            self.battery = self.battery + 1
        else:
            self.battery = self.battery - 1
    
#        
            
