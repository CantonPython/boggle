#!/usr/bin/python3

import tkinter as tk
from boggle_dice import BoggleDice
from boggle_solver import BoggleSolver

class BoggleApp(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.rows = 4
        self.cols = 4
        self.dice = BoggleDice()
        self.solver = BoggleSolver('boggle_words.txt')
        self.words = []
        self.running = False

        self.root = root
        self.root.title('Boggle')
        self.grid()
        self.create_widgets()
        self.paint_canvas()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=480, height=480, bg='green')
        self.panel = self.create_panel_widgets()

        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.panel.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N)

    def create_panel_widgets(self):
        self.var_word = tk.StringVar()
        self.var_words = tk.StringVar()
        self.var_found = tk.StringVar()
        self.var_missed = tk.StringVar()

        panel = tk.Frame(self)
        button_action = tk.Button(panel, command=self.shake, text='Shake!')
        self.button_action = button_action # toggles
        button_quit = tk.Button(panel, command=self.quit, text='Quit')
        entry_word = tk.Entry(panel, width=32, textvariable=self.var_word)
        button_ok = tk.Button(panel, text='Ok')
        self.root.bind('<Return>', self.add_word)
        button_ok.bind('<Button-1>', self.add_word)
        message_words = tk.Message(panel, width=280, textvariable=self.var_words)
        message_found = tk.Message(panel, width=280, textvariable=self.var_found)
        message_missed = tk.Message(panel, width=280, textvariable=self.var_missed)

        button_action.grid(row=0, column=0)
        button_quit.grid(row=0, column=1)
        entry_word.grid(row=2, column=0)
        button_ok.grid(row=2, column=1)
        message_words.grid(row=5)
        message_found.grid(row=6)
        message_missed.grid(row=7)

        return panel

    def paint_canvas(self, letters=''):
        MARGIN = 64
        PAD = 10
        WIDTH = 80
        HEIGHT = 80
        COLOR = 'white'
        FONT = ('Times', 18)
        for row in range(self.rows):
            for col in range(self.cols):
                y0 = MARGIN + (row * (WIDTH + PAD))
                x0 = MARGIN + (col * (HEIGHT + PAD))
                y1 = y0 + WIDTH
                x1 = x0 + HEIGHT
                y2 = y0 + (WIDTH/2)
                x2 = x0 + (HEIGHT/2)
                i = (row  * self.rows) + col
                try:
                    ch = letters[i].upper()
                except IndexError:
                    ch = ''
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=COLOR)
                self.canvas.create_text(x2, y2, font=FONT, text=ch)

    def quit(self):
        self.root.destroy()

    def clear(self):
        self.var_word.set('')
        self.var_words.set('')
        self.var_found.set('')
        self.var_missed.set('')
        self.words = []

    def shake(self):
        self.button_action.configure(text='Solve', command=self.solve)
        self.clear()
        self.letters = self.dice.shake()
        self.paint_canvas(self.letters)
        self.running = True

    def add_word(self, event):
        if not self.running:
            return
        word = self.var_word.get().strip()
        self.var_word.set('')
        if len(word) > 2 and word not in self.words:
            self.words.append(word)
            self.var_words.set(' '.join(self.words))

    def solve(self):
        if not self.running:
            return
        self.button_action.configure(text='Shake!', command=self.shake)
        self.solver.solve(self.letters)
        solution = set(self.solver.found())

        words = set(self.words)
        found = words & solution
        missed = solution - words

        found_text = 'Found:\n' + ' '.join(list(found))
        missed_text = 'Missed:\n' + ' '.join(list(missed))

        self.var_found.set(found_text)
        self.var_missed.set(missed_text)

        self.running = False


def main():
    root = tk.Tk()
    BoggleApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
