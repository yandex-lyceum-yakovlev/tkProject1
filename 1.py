import tkinter


def f(event):
    c.create_oval((event.x - 10, event.y - 10), (event.x + 10, event.y + 10), fill="red")


def keydown(event):
    print(event.keysym)


w = tkinter.Tk()
c = tkinter.Canvas(width=600, height=600, background="white")
c.pack()
c.bind("<Motion>", f)
w.bind("<KeyPress>", keydown)
w.mainloop()
