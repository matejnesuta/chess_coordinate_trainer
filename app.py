import tkinter as tk 
from tkinter import messagebox
import random 
import json

class App(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        self.title("Chess Coordinate Trainer") 
        self.geometry("1050x900") 
        self.resizable(0, 0)
        self.configure(background="#bfbfbf")
        self.img = tk.PhotoImage(file="pixel.png") 
        self.ribbon()
        self.chessboard()
        self.souradnice = tk.StringVar()
        self.souradnice.set("...")
        self.currentCoordinate=tk.Label(textvariable=self.souradnice, width="8", font=("Helvetica, 40"),borderwidth="1", relief="solid")
        self.currentCoordinate.grid(row=1,column=8, columnspan=4)
        self.timeDescription=tk.Label(text="Zbývající čas:", font=("Helvetica, 20"),borderwidth="1", relief="solid", padx="10")
        self.timeDescription.grid(row=2, column=8,columnspan=2)
        self.time = tk.DoubleVar()
        self.time.set(00.00)
        self.cas=tk.Label(textvariable=self.time, width="4", font=("Helvetica, 20"), borderwidth="1", relief="solid")
        self.cas.grid(row=2,column=10, columnspan=2)
        self.gameOn=0
        self.scoreDescription=tk.Label(text="Skóre:", font=("Helvetica, 20 "),borderwidth="1", relief="solid", padx="53")
        self.scoreDescription.grid(row=3, column=8,columnspan=2)
        self.score=tk.IntVar()
        self.score.set(0)
        self.scoreLabel=tk.Label(textvariable=self.score, font=("Helvetica, 20"),borderwidth="1", relief="solid", width="4")
        self.scoreLabel.grid(row=3, column=10, columnspan=2)
        self.index=-1
        self.player = 0
        self.barva=tk.StringVar()
        self.barva.set("Bílá")
        self.pohled = tk.Label(textvariable=self.barva, width="8", font=("Helvetica, 40"),borderwidth="1", relief="solid")   
        self.pohled.grid(row=4, column=8, columnspan=4)     
    
    "Tyto dve funkce určujou pohled hráče."
    def whiteplayer(self):
        self.player = 0
        self.barva.set("Bílá")
    def blackplayer(self):
        self.player = 1
        self.barva.set("Černá")

    def settings(self):
        self.win = tk.Toplevel()
        self.win.wm_title("Nastavení")
        self.win.wm_geometry = ("200x400")
        self.win.grab_set()
        self.win.resizable(0,0)
        perspektiva = tk.Label(self.win, text="Nastavení perspektivy: ")
        perspektiva.grid(row=0, column=0)
        white=tk.Button(self.win, text="Bílá", command=self.whiteplayer)
        white.grid(row=0, column=1)
        black=tk.Button(self.win, text="Černá", command=self.blackplayer)
        black.grid(row=0, column=2)
        souradnice=tk.Label(self.win, text="Vypnutí/zapnutí souřadnic: ")
        souradnice.grid(row=1, column=0)

    def info(self):
        self.win = tk.Toplevel()
        self.win.wm_title("Info")
        self.win.grab_set()
        l = tk.Label(self.win, text="Tato krásná věc byla vytvořena jako můj domácí úkol. \n\n “The blunders are all there on the board, waiting to be made.” - Savielly Tartakower")
        l.grid(row=0, column=0)
    
    def leaderboard(self):
        self.win = tk.Toplevel()
        self.win.geometry("200x200")
        self.win.resizable(0,0)
        self.win.wm_title("Žebříček")
        self.win.grab_set()
        self.win.configure(background="#bfbfbf")
        string=tk.StringVar()
        with open("leaderboard.json", "r") as inside:
            data = json.load(inside)
        print (data[0]["jmeno"])
        text = tk.Label(self.win, font=("Helvetica, 20"), textvariable=string, state='normal', height=20, width=60)
        for i in range (1,6):
            string.set(string.get()+str(i)+".  "+data[i-1]["jmeno"]+"  "+str(data[i-1]["score"])+"\n")
        text.pack()

    """Vykreslení šachovnice samotné. Každé políčko je vyvoláno jako tlačítko a přidáno do listu. 
    Tlačítka vrací index od 0-63 a ten se porovnává s náhodně vygenerovaným indexem, který určuje souřadnici, jenž musí hráč najít na šachovnici."""
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
                
            for y in range (0,8):
                if y % 2 == 1:
                    b=tk.Button(image=self.img,compound=tk.LEFT,background="black", activebackground="grey",height=94,width=94,command=lambda num=i: self.callback(num))
                else:
                    b=tk.Button(image=self.img,compound=tk.LEFT,background="white", activebackground="grey",height=94,width=94,command=lambda num=i: self.callback(num))
                self.buttons.append(b)
                self.buttons[2*8*x+y+8].grid(row=8-y,column=2*x+1)
                i=i+1

    def game(self):
        if self.gameOn==0:
            self.gameOn=1
            self.startname.set("Storno")
            #cas je nastavenej v milisekundách, aby mezi vypršením časomíry a vyskočením okna s výsledkem nebyla 1 sekundová odezva, jelikož funkce časovače volala sama sebe po jedné sekundě a do toho odčítala proměnnou času. 
            #1 sekunda byla dost na to, aby člověk stihl zmáčknout start a storno po sobě a rozbít tak časovač.
            self.timer=30000
            self.index=random.randint(0,63)
            self.souradnice.set(self.coordinates[self.index])
            self.time.set(self.timer)
            self.stopky()
        else:
            #else větev, pokud by se hráč rozhodl stronovat hru
            self.gameOn=0
            self.souradnice.set("...")
            self.score.set(0)
            self.timer=0.0
            self.time.set(00.00)
            self.startname.set("Start")

    def stopky(self):
        if self.timer >= 0:
            if self.timer % 1000 == 0:
                self.time.set(self.timer/1000)
            self.timer-=1
            self.after(1, self.stopky)
        else:
            self.gameOn=0
            self.souradnice.set("...")
            messagebox.showinfo("Konec hry","Dosažené skóre: "+str(self.score.get()))
            self.score.set(0)
            self.startname.set("Start")
    
    def callback(self, click):
            print(click)
            if self.gameOn == 1:  
                if self.player == 0:   
                    if click==self.index:
                        self.score.set(self.score.get()+1)
                        self.index=random.randint(0,63)
                        self.souradnice.set(self.coordinates[self.index])
                elif self.player == 1:   
                    if 63-click==self.index:
                        self.score.set(self.score.get()+1)
                        self.index=random.randint(0,63)
                        self.souradnice.set(self.coordinates[self.index])
            else:
                pass    
                
    def ribbon(self):
        self.startname=tk.StringVar()
        self.startname.set("Start")
        self.start=tk.Button(textvariable=self.startname, image=self.img, compound=tk.LEFT, height=21, width=192, command=lambda:self.game())
        self.options=tk.Button(text="Nastavení", image=self.img, compound=tk.LEFT, height=21, width=192, command=lambda:self.settings())
        self.vysledky=tk.Button(text="Tabulka výsledků", image=self.img, compound=tk.LEFT, height=21, width=192, command=self.leaderboard)
        self.about=tk.Button(text="O aplikaci", image=self.img, compound=tk.LEFT, height=21, width=192, command=lambda:self.info())
        self.start.grid(row=0, column=0, columnspan=2)
        self.options.grid(row=0, column=2, columnspan=2)
        self.vysledky.grid(row=0, column=4, columnspan=2)
        self.about.grid(row=0, column=6, columnspan=2)
        
if __name__ == "__main__": 
    app = App() 
    app.mainloop()