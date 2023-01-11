import tkinter


def draw():
    c.create_rectangle((0, 0), (600, 600), fill="white")
    for i in range(m):
        for j in range(n):
            if board[i][j] in colors:
                color = colors[board[i][j]]
            else:
                color = "white"
            c.create_rectangle((i * cw + 2, j * ch + 2), ((i + 1) * cw, (j + 1) * ch), outline="black", fill=color)
            c.create_text(i * cw + cw // 2, j * ch + ch // 2, text=board[i][j])


def f(event):
    cj = event.x // cw
    ci = event.y // ch
    board[cj][ci] += 1
    draw()


w = tkinter.Tk()
n, m = 12, 12
cw, ch = 600 // n, 600 // m
board = [[0] * n for i in range(m)]
colors = {0: "white", 1: "red", 2: "green",  3: "blue"}
c = tkinter.Canvas(width=600, height=600, background="white")
c.pack()
draw()
c.bind("<Button-1>", f)
w.mainloop()
