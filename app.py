import tkinter as tk 
import sys
import random 
import time
class App(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        self.title("Chess Coordinate Trainer") 
        self.geometry("1000x1000") 
        self.resizable(0, 0)
        self.configure(background="#fba800")
        self.img = tk.PhotoImage(file="pixel.png") 
        self.ribbon()
        self.chessboard()
        self.souradnice = tk.StringVar()
        self.souradnice.set("...")
        self.currentCoordinate=tk.Label(textvariable=self.souradnice, font=("Helvetica", 25))
        self.currentCoordinate.grid(row=1,column=8, columnspan=2)
        self.time = tk.DoubleVar()
        self.time.set(00.00)
        self.cas=tk.Label(textvariable=self.time, font=("Helvetica, 40"))
        self.cas.grid(row=2,column=8, columnspan=2)
        self.gameOn=0
        
    
    
    def zavreni(self):
        self.win.destroy()

    def settings(self):
        self.win = tk.Toplevel()
        self.win.wm_title("Nastavení")
        self.win.wm_geometry = ("200x400")
        self.win.grab_set()
        self.win.resizable(0,0)
        perspektiva = tk.Label(self.win, text="Nastavení perspektivy: ")
        perspektiva.grid(row=0, column=0)
        white=tk.Button(self.win, text="Bílá")
        white.grid(row=0, column=1)
        black=tk.Button(self.win, text="Černá")
        black.grid(row=0, column=2)
        souradnice=tk.Label(self.win, text="Vypnutí/zapnutí souřadnic: ")
        souradnice.grid(row=1, column=0)
        b = tk.Button(self.win, text="Okay", command=self.zavreni)
        b.grid(row=2, column=0)

    def info(self):
        self.win = tk.Toplevel()
        self.win.wm_title("Window")
        self.win.grab_set()
        l = tk.Label(self.win, text="Tato krásná věc byla vytvořena jako můj domácí úkol.")
        l.grid(row=0, column=0)

        b = tk.Button(self.win, text="Okay", command=self.zavreni)
        b.grid(row=1, column=0)
   
    
    
    def callback(self, click):
            print(self.coordinates[click])
            if self.gameOn == 1:
                pass
    
    
    def chessboard(self):     
        self.coordinates = ("A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8","F1","F2","F3","F4","F5","F6","F7","F8","G1","G2","G3","G4","G5","G6","G7","G8","H1","H2","H3","H4","H5","H6","H7","H8")
        self.buttons = []
        i=0
        for x in range(0,4):
            for y in range (0,8):
                if y % 2 == 0:
                    b=tk.Button(image=self.img,compound=tk.LEFT,background="black", activebackground="grey",height=94,width=94,command=lambda num=i: self.callback(num))
                else:
                    b=tk.Button(image=self.img,compound=tk.LEFT,background="white", activebackground="grey",height=94,width=94,command=lambda num=i: self.callback(num))
                self.buttons.append(b)
                self.buttons[2*8*x+y].grid(row=8-y,column=2*x)
                i=i+1
                print(2*8*x+y)
                
            for y in range (0,8):
                if y % 2 == 1:
                    b=tk.Button(image=self.img,compound=tk.LEFT,background="black", activebackground="grey",height=94,width=94,command=lambda num=i: self.callback(num))
                else:
                    b=tk.Button(image=self.img,compound=tk.LEFT,background="white", activebackground="grey",height=94,width=94,command=lambda num=i: self.callback(num))
                self.buttons.append(b)
                self.buttons[2*8*x+y+8].grid(row=8-y,column=2*x+1)
                i=i+1
                print(2*8*x+y+8)
    def idk(self):
        pass

    def game(self):
        timer=30.00
        index=random.randint(0,63)
        self.souradnice.set(self.coordinates[index])
        while timer > 0.00:
            time.sleep(0.1) 
            timer-00.10
            self.time.set(timer)
            
                
    def ribbon(self):
        self.start=tk.Button(text="Start", image=self.img, compound=tk.LEFT, height=21, width=192, command=lambda:self.game())
        self.options=tk.Button(text="Nastavení", image=self.img, compound=tk.LEFT, height=21, width=192, command=lambda:self.settings())
        self.vysledky=tk.Button(text="Tabulka výsledků", image=self.img, compound=tk.LEFT, height=21, width=192, )
        self.about=tk.Button(text="O aplikaci", image=self.img, compound=tk.LEFT, height=21, width=192, command=lambda:self.info())
        self.exit=tk.Button(text="Ukončit", image=self.img,compound=tk.LEFT, height=21, width=192, command=sys.exit)
        
        self.start.grid(row=0, column=0, columnspan=2)
        self.options.grid(row=0, column=2, columnspan=2)
        self.vysledky.grid(row=0, column=4, columnspan=2)
        self.about.grid(row=0, column=6, columnspan=2)
        self.exit.grid(row=0, column=8, columnspan=2)  
        

    


if __name__ == "__main__": 
    app = App() 
    app.mainloop()