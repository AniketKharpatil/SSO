from tkinter import Tk, Frame, Button, Label

class GUI:

    def __init__(self, root):
        self.root = root # root is a passed Tk object
        self.button = Button(self.root, text="Push me", command=self.removethis)
        self.button.pack()
        self.frame = Frame(self.root)
        self.frame.pack()
        self.label = Label(self.frame, text="I'll be destroyed soon!")
        self.label.pack()

    def removethis(self):
        self.frame.destroy()

root = Tk()
window = GUI(root)
root.mainloop()