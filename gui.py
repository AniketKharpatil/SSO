from dictionary import Dictionary
from tkinter import *
from time import strftime


def newdict():
    root1=Tk()
    root1.title("Online Dictionary")
    root1.geometry("500x600")


    inst_label=Label(root1,text="What word do you want to look up?",height=3,font=(None, 15)).pack(fill=X,side=TOP)


    e=Entry(root1,width=35,borderwidth=5,font=(None, 15))
    e.pack(fill=X,side=TOP)

    def find_command():
        global short_label
        global long_label
        d = Dictionary(e.get())
        try:
            short_string = "SHORT MEANING \n"+"_"*20+"\n"+d.get_short_meaning() + "\n"
            long_string = "LONG MEANING \n"+"_"*20+"\n"+d.get_long_meaning() + "\n"
        except:
            short_string="No Meaning Found"
            long_string = " "
        short_label=Label(root1,text=short_string,wraplength=400)
        short_label.pack(fill=X)
        long_label=Label(root1,text=long_string,wraplength=400)
        long_label.pack(fill=X)

    def reset():
        e.delete(0, 'end')
        short_label.destroy()
        long_label.destroy()

    find_button=Button(root1,text="Reset",command=reset,bg="Black",fg="White",height=2,font=(None, 15),borderwidth=5)
    find_button.pack(fill=X,side=BOTTOM)
    find_button=Button(root1,text="Find",command=find_command,bg="Black",fg="White",height=2,font=(None, 15),borderwidth=5)
    find_button.pack(fill=X,side=BOTTOM)

    root1.mainloop()


def digiclk():
    root2 = Tk()  # Creates tkinter window
    root2.title("Digital Clock")  # Adds title to tkinter window

    # Function used to display time on the label
    def time():
        string = strftime("%H:%M:%S %p")
        lbl.config(text = string)
        lbl.after(1000, time)

    # Styling the label widget which displays the clock
    lbl = Label(root2, font = ("arial", 75, "bold"),bg="red",fg="white")

    # Pack method in tkinter packs widgets into rows or columns. Positions label
    lbl.pack(anchor = "center",fill = "both",expand=1)

    time()
    root2.mainloop()

def run_service():
    root_1=Tk()
    root_1.title("Services")
    root_1.geometry("600x550")
    Label(master=root_1, text="Choose any option from below", wraplength=400).pack()
    Button(root_1,text="Digital clock",command=digiclk).pack(padx=10,pady=10)
    Button(root_1,text="Use Dictionary ",command=newdict).pack(padx=10,pady=10)
    root_1.mainloop()














