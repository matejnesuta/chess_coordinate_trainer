import tkinter as tk 
import sys
import random 
import threading 

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
        self.time = tk.StringVar()
        self.time.set("00:00")
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
            print(click)
            if self.gameOn == 1:
                pass
    
    
    def chessboard(self):     
        A1=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",text="A1",foreground="white",anchor="sw",height=94,width=94,command=lambda:self.callback("A1"))
        A2=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",text="A2",foreground="black",anchor="w",height=94,width=94,command=lambda:self.callback("A2"))
        A3=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",text="A3",foreground="white",anchor="w",height=94,width=94,command=lambda:self.callback("A3"))
        A4=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",text="A4",foreground="black",anchor="w",height=94,width=94,command=lambda:self.callback("A4"))
        A5=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",text="A5",foreground="white",anchor="w",height=94,width=94,command=lambda:self.callback("A5"))
        A6=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",text="A6",foreground="black",anchor="w",height=94,width=94,command=lambda:self.callback("A6"))
        A7=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",text="A7",foreground="white",anchor="w",height=94,width=94,command=lambda:self.callback("A7"))
        A8=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",text="A8",foreground="black",anchor="w",height=94,width=94,command=lambda:self.callback("A8"))
        B1=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",text="B1",foreground="black",anchor="s",height=94,width=94,command=lambda:self.callback("B1"))
        B2=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("B2"))
        B3=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("B3"))
        B4=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("B4"))
        B5=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("B5"))
        B6=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("B6"))
        B7=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("B7"))
        B8=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("B8"))
        C1=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",text="C1",foreground="white",anchor="s",height=94,width=94,command=lambda:self.callback("C1"))
        C2=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("C2"))
        C3=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("C3"))
        C4=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("C4"))
        C5=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("C5"))
        C6=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("C6"))
        C7=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("C7"))
        C8=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("C8"))
        D1=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",text="D1",foreground="black",anchor="s",height=94,width=94,command=lambda:self.callback("D1"))
        D2=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("D2"))
        D3=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("D3"))
        D4=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("D4"))
        D5=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("D5"))
        D6=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("D6"))
        D7=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("D7"))
        D8=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("D8"))
        E1=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",text="E1",foreground="white",anchor="s",height=94,width=94,command=lambda:self.callback("E1"))
        E2=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("E2"))
        E3=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("E3"))
        E4=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("E4"))
        E5=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("E5"))
        E6=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("E6"))
        E7=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("E7"))
        E8=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("E8"))
        F1=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",text="F1",foreground="black",anchor="s",height=94,width=94,command=lambda:self.callback("F1"))
        F2=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("F2"))
        F3=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("F3"))
        F4=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("F4"))
        F5=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("F5"))
        F6=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("F6"))
        F7=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("F7"))
        F8=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("F8"))
        G1=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",text="G1",foreground="white",anchor="s",height=94,width=94,command=lambda:self.callback("G1"))
        G2=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("G2"))
        G3=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("G3"))
        G4=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("G4"))
        G5=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("G5"))
        G6=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("G6"))
        G7=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("G7"))
        G8=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("G8"))
        H1=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",text="H1",foreground="black",anchor="s",height=94,width=94,command=lambda:self.callback("H1"))
        H2=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("H2"))
        H3=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("H3"))
        H4=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("H4"))
        H5=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("H5"))
        H6=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("H6"))
        H7=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:self.callback("H7"))
        H8=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:self.callback("H8"))
        
        chessboard=((A1,A2,A3,A4,A5,A6,A7,A8),(B1,B2,B3,B4,B5,B6,B7,B8),(C1,C2,C3,C4,C5,C6,C7,C8),(D1,D2,D3,D4,D5,D6,D7,D8),(E1,E2,E3,E4,E5,E6,E7,E8),(F1,F2,F3,F4,F5,F6,F7,F8),(G1,G2,G3,G4,G5,G6,G7,G8),(H1,H2,H3,H4,H5,H6,H7,H8))        
        for x in range (0,8):
            for y in range (0,8):
                chessboard[x][y].grid(row=8-y,column=x)

        self.coordinates = ("A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8","F1","F2","F3","F4","F5","F6","F7","F8","G1","G2","G3","G4","G5","G6","G7","G8","H1","H2","H3","H4","H5","H6","H7","H8")

        


    def game(self): 
        score = 0
        pokus = 0
        index = 0
        
        time = 30
        while time:
            index=random.randint(0,63)
            self.souradnice.set(self.coordinates[index])
            self.tmp=""
            if self.tmp == self.coordinates[index]:
                score=score+1
                pokus=pokus+1
            else: 
                pokus=pokus+1   
                
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