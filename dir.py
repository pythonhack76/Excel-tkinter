import os
from tkinter import *
from tkinter import messagebox

#=============================== FINESTRA  ===================================================#

root = Tk()
root.title("CreDir")
root.geometry("400x500")
p1 = PhotoImage(file = 'chees.png')
 
# Setting icon of master window
root.iconphoto(False, p1)
copyright_symbol = u"\u00A9"
text = Text(root)

#dati del modulo
dir_var=StringVar()

#funzioni del modulo
def submit():

    dir = dir_var.get()

    print("la directory è: " + dir)

    dir_var.set("inserisci directory nuova!")


#=============================== FUNZIONI  ===================================================#

def percorso_dir():
    percorso = (os.getcwd())
    print("attuale percorso PATH", percorso)
    p1 = str(percorso)

    text.insert(INSERT, p1)
    text.insert(END, "")
    text.pack(padx =2, pady=2, expand = False, fill = BOTH)


def createDir():
    directory = dir_var.get()
    if(directory != 0):
        messagebox.showerror("Errore Programma", "Non puoi lasciare in bianco!")
    else:
        parent_dir = (os.getcwd()) 
        path = os.path.join(parent_dir, directory)
        os.makedirs(path)
    
        print("Directory '% s' creata" % directory)


    

    


#=============================== LABELFRAME  =================================================#

label_frame = LabelFrame(root, text= 'Struttura  Window')
label_frame.pack(expand='yes', fill = 'both')



#=============================== LABEL  ===================================================#
lbl_title = Label(root, text="Crea Directory | " + copyright_symbol + " Luca Rulvoni 2021", font = '50')
lbl_title.pack()
lb1 = Label(root, text="crea directory", font="20").place(x=30, y=60)
directory_input = Entry(root, textvariable=dir_var, relief='sunken', bd='5', width=30, font=('calibre',10,'bold')).place(x = 130, y = 60)

#=============================== BOTTONI ===================================================#
invio_button = Button(root, text="CREA", padx=10, pady=10, width='30', font="50", bd='5', background='grey', foreground='white', command=createDir).place(x=40, y=130)
chiudi_button = Button(root, text="Chiudi", padx=10, pady=10, background='red', bd='5', foreground='white', width='30', font='50', command=root.destroy ).place(x=40, y=190)

dir_button = Button(root, text="DIR NOW", padx=10, pady=10, background='blue', bd='5', foreground='white', width='30', font='50', command=percorso_dir ).place(x=40, y=250)
#=============================== START ===================================================#
root.mainloop()