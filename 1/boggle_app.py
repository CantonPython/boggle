#!/usr/bin/python3

import tkinter as tk
import boggle_dice

class BoggleApp(tk.Frame):
    def __init__(self, root, rows=4, cols=4):
        super().__init__(root)
        self.rows = rows
        self.cols = cols
        self.parent = root
        self.parent.title('Boogle')
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=600, height=600, bg='green')
        self.panel = tk.Frame(self, width=400, height=600, bg='white')
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.panel.grid(row=0, column=1, padx=10, pady=10)

        shake = tk.Button(self.panel, text='Shake!', command=self.shake)
        quit = tk.Button(self.panel, text='Quit', command=self.quit)
        shake.grid(row=0, column=0)
        quit.grid(row=0, column=1)

        self.paint_canvas()

    def quit(self):
        print('Bye!')
        self.parent.destroy()

    def shake(self):
        print('Shake it')
        # randomize
        self.paint_canvas()

    def paint_canvas(self):
        MARGIN = 20
        PAD = 10
        WIDTH = 80
        HEIGHT = 80
        BGCOLOR = 'white'
        FONT = ('Times', 18)
        dice = boggle_dice.shake()
        for row in range(self.rows):
            for col in range(self.cols):
                y0 = MARGIN + (row * (WIDTH + PAD))
                x0 = MARGIN + (col * (HEIGHT + PAD))
                y1 = y0 + WIDTH
                x1 = x0 + HEIGHT
                y2 = y0 + (WIDTH/2)
                x2 = x0 + (HEIGHT/2)
                i = (row  * self.cols) + col
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=BGCOLOR)
                self.canvas.create_text(x2, y2, font=FONT, text=dice[i])


def main():
    root = tk.Tk()
    BoggleApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
