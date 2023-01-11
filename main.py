import tkinter


w = tkinter.Tk()
c = tkinter.Canvas(width=600, height=600, background="white")
c.pack()
for i in range(50, 600, 50):
    c.create_line((i, 0), (i, 600), fill="red")
    c.create_line((0, i), (600, i), fill="red")
# c.create_rectangle((100, 100), (200, 300), outline="green")
# c.create_oval((100, 100), (200, 300), outline="blue")
w.mainloop()
