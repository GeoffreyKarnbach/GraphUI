from tkinter import*
import math

class Graph:

    def __init__(self,table):
        self.connections=table
        self.fen=Tk()
        self.can=Canvas(self.fen)
        self.can.grid()

    def set_colors(self,colors):
        self.colors=colors

    def show_connection(self):
        self.liste=[]
        for loop in range(len(self.connections)):
            for lopp in range(len(self.connections)):
                if self.connections[loop][lopp]==1:
                    self.liste.append((loop,lopp))
        print(self.liste)

    def polygon(self,sides, radius=100, rotation=math.pi):
        one_segment = math.pi * 2 / sides
        points = [(math.sin(one_segment * i + rotation) * radius,math.cos(one_segment * i + rotation) * radius) for i in range(sides)]

        return points

    def show_graph(self,size):

        self.can.config(width=size*3,height=size*3)
        self.size=size+50

        self.coords=self.polygon(len(self.connections),radius=size)
        self.fen.title("Graph")


        for loop in range(len(self.connections)):
            self.can.create_oval(self.size+self.coords[loop][0]-10,self.size+self.coords[loop][1]-10,self.size+self.coords[loop][0]+10,self.size+self.coords[loop][1]+10,fill=self.colors[loop])
            self.can.create_text(self.size+self.coords[loop][0],self.size+self.coords[loop][1],text=str(loop+1))


        for loop in range(len(self.liste)):
            x1=self.size+self.coords[self.liste[loop][0]][0]
            y1=self.size+self.coords[self.liste[loop][0]][1]
            x2=self.size+self.coords[self.liste[loop][1]][0]
            y2=self.size+self.coords[self.liste[loop][1]][1]
            self.can.create_line(x1,y1,x2,y2)
        self.fen.mainloop()



