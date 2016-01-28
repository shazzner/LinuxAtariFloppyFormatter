from Tkinter import *

class LaffGui:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="Load ST Disk Image", command=self.say_hi)
            #frame, text="Load ST Disk Image", fg="red", command=frame.quit

        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"
