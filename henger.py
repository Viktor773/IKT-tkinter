from tkinter import *
foablak = Tk()

def kiszamit():
    p = 3.14
    r = int(Sugarimport.get())
    m = int(Magassagimport.get())
    e = p*r**2*m
    Terfogatkiad.delete(0, END)
    Terfogatkiad.insert(0+int(e))

Sugar = Label(foablak, text="Sugár")
Sugar.pack()
Sugarimport = Entry(foablak)
Sugarimport.pack()
Magassag=Label(foablak,text="Magasság")
Magassag.pack()
Magassagimport=Entry(foablak)
Magassagimport.pack()
Gomb = Button(foablak, text="Kiszámít", command=kiszamit)
Gomb.pack()
Terfogat = Label(foablak, text="Térfogat")
Terfogat.pack()
Terfogatkiad = Entry(foablak)
Terfogatkiad.pack()
Vashenger = Label(foablak, text="Vashenger")
Vashenger.pack()
Vashengerkiad = Entry(foablak)
Vashengerkiad.pack()
Fahenger = Label(foablak, text="Fahenger")
Fahenger.pack()
Fahengerkiad = Entry(foablak)
Fahengerkiad.pack()



foablak.mainloop()