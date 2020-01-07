import tkinter as tk 
import sys

class App(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        self.title("Úkol do PCV") 
        self.geometry("1000x1000") 
        self.resizable(0, 0)
        self.configure(background="#fba800")
        self.img = tk.PhotoImage(file="pixel.png") 
        souradnice=""
        self.ribbon()
        self.chessboard()
        
    def ribbon(self):
        self.start=tk.Button(text="Start", image=self.img, compound=tk.LEFT, height=21, width=192)
        self.options=tk.Button(text="Nastavení", image=self.img, compound=tk.LEFT, height=21, width=192)
        self.vysledky=tk.Button(text="Tabulka výsledků", image=self.img, compound=tk.LEFT, height=21, width=192)
        self.about=tk.Button(text="O aplikaci", image=self.img, compound=tk.LEFT, height=21, width=92)
        self.exit=tk.Button(text="Ukončit", image=self.img,compound=tk.LEFT, height=21, width=92, command=sys.exit)
        self.start.grid(row=0, column=0, columnspan=2)
        self.options.grid(row=0, column=2, columnspan=2)
        self.vysledky.grid(row=0, column=4, columnspan=2)
        self.about.grid(row=0, column=6)
        self.exit.grid(row=0, column=7)  
    
    
    
    def chessboard(self):    
        souradnice=""
        

        def callback(click):
            click=souradnice
        
        def picovina(click):
            print(click)  

        idk=tk.Label(text=souradnice)
        idk.grid(row=0, column=8)
        
        
        self.A1=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:picovina("A1"))
        self.A2=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("A2"))
        self.A3=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("A3"))
        self.A4=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("A4"))
        self.A5=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("A5"))
        self.A6=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("A6"))
        self.A7=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("A7"))
        self.A8=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("A8"))
        self.B1=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("B1"))
        self.B2=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("B2"))
        self.B3=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("B3"))
        self.B4=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("B4"))
        self.B5=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("B5"))
        self.B6=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("B6"))
        self.B7=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("B7"))
        self.B8=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("B8"))
        self.C1=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("C1"))
        self.C2=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("C2"))
        self.C3=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("C3"))
        self.C4=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("C4"))
        self.C5=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("C5"))
        self.C6=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("C6"))
        self.C7=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("C7"))
        self.C8=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("C8"))
        self.D1=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("D1"))
        self.D2=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("D2"))
        self.D3=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("D3"))
        self.D4=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("D4"))
        self.D5=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("D5"))
        self.D6=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("D6"))
        self.D7=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("D7"))
        self.D8=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("D8"))
        self.E1=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("E1"))
        self.E2=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("E2"))
        self.E3=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("E3"))
        self.E4=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("E4"))
        self.E5=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("E5"))
        self.E6=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("E6"))
        self.E7=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("E7"))
        self.E8=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("E8"))
        self.F1=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("F1"))
        self.F2=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("F2"))
        self.F3=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("F3"))
        self.F4=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("F4"))
        self.F5=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("F5"))
        self.F6=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("F6"))
        self.F7=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("F7"))
        self.F8=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("F8"))
        self.G1=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("G1"))
        self.G2=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("G2"))
        self.G3=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("G3"))
        self.G4=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("G4"))
        self.G5=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("G5"))
        self.G6=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("G6"))
        self.G7=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("G7"))
        self.G8=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("G8"))
        self.H1=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("H1"))
        self.H2=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("H2"))
        self.H3=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("H3"))
        self.H4=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("H4"))
        self.H5=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("H5"))
        self.H6=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("H6"))
        self.H7=tk.Button(image=self.img,compound=tk.LEFT,bg="white",activebackground="grey",height=94,width=94,command=lambda:callback("H7"))
        self.H8=tk.Button(image=self.img,compound=tk.LEFT,bg="black",activebackground="grey",height=94,width=94,command=lambda:callback("H8"))
        
        self.chessboard=((self.A1,self.A2,self.A3,self.A4,self.A5,self.A6,self.A7,self.A8),(self.B1,self.B2,self.B3,self.B4,self.B5,self.B6,self.B7,self.B8),(self.C1,self.C2,self.C3,self.C4,self.C5,self.C6,self.C7,self.C8),(self.D1,self.D2,self.D3,self.D4,self.D5,self.D6,self.D7,self.D8),(self.E1,self.E2,self.E3,self.E4,self.E5,self.E6,self.E7,self.E8),(self.F1,self.F2,self.F3,self.F4,self.F5,self.F6,self.F7,self.F8),(self.G1,self.G2,self.G3,self.G4,self.G5,self.G6,self.G7,self.G8),(self.H1,self.H2,self.H3,self.H4,self.H5,self.H6,self.H7,self.H8))        
        for x in range (0,8):
            for y in range (0,8):
                self.chessboard[7-x][y].grid(row=x+1,column=y)
        
if __name__ == "__main__": 
    app = App() 
    app.mainloop()