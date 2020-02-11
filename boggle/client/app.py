#!/usr/bin/python3

import os
import time
import tkinter as tk
from boggle.shared.dice import BoggleDice
from boggle.shared.solver import BoggleDictionary
from boggle.shared.solver import BoggleSolver

class BoggleTimer(tk.Label):
    def __init__(self, parent):
        self.var_countdown = tk.StringVar()
        super().__init__(parent, width=6, textvariable=self.var_countdown)
        self.running = False

    def start(self, seconds, callback):
        if self.running:
            return
        self.update(seconds)
        now = time.time()
        self.expired = now + seconds
        self.callback = callback
        self.after(1000, self.tick)
        self.running = True

    def update(self, remaining):
        minutes = int(remaining / 60.0)
        seconds = int(remaining % 60.0)
        self.var_countdown.set('%d:%02d' % (minutes, seconds))

    def tick(self):
        now = time.time()
        remaining = int(self.expired - now)
        if remaining > 0:
            self.update(remaining)
            self.after(1000, self.tick)
        else:
            self.update(0)
            self.running = False
            self.callback()


class BoggleApp(tk.Frame):

    # Word score table
    points = {0:0, 1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}

    def __init__(self, root):
        super().__init__(root)

        self.rows = 4
        self.cols = 4
        self.dice = BoggleDice()
        self.dictionary = BoggleDictionary(filename=os.path.expanduser('~/.boggle/words.txt'))
        self.solver = BoggleSolver(self.dictionary)
        self.words = []
        self.letters = []
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
        self.panel.grid(row=0, column=1, padx=10, pady=10, sticky='n')

    def create_panel_widgets(self):
        self.var_word = tk.StringVar()
        self.var_message = tk.StringVar()

        panel = tk.Frame(self)
        self.button_action = tk.Button(panel, command=self.shake, text='Shake!')
        self.timer = BoggleTimer(panel)
        entry_word = tk.Entry(panel, width=32, textvariable=self.var_word)
        button_ok = tk.Button(panel, command=self.add_word, text='Ok')
        self.root.bind('<Return>', self.add_word)
        message = tk.Message(panel, width=280, anchor='w', textvariable=self.var_message)
        button_quit = tk.Button(panel, command=self.quit, text='Quit')

        self.button_action.grid(row=0, column=0, sticky='w')
        self.timer.grid(row=0, column=1)
        entry_word.grid(row=2, column=0)
        button_ok.grid(row=2, column=1)
        message.grid(row=3, columnspan=2, stick='w')
        button_quit.grid(row=6, column=1)

        entry_word.focus_set()

        return panel

    def paint_canvas(self, path=None):
        if path is None:
            path = []
        MARGIN = 64
        PAD = 10
        WIDTH = 80
        HEIGHT = 80
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
                    ch = self.letters[i].upper()
                except IndexError:
                    ch = ''
                if i in path:
                    fg,bg = 'white','blue'
                else:
                    fg,bg = 'black','white'
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=bg)
                self.canvas.create_text(x2, y2, font=FONT, text=ch, fill=fg)

    def quit(self):
        self.root.destroy()

    def clear(self):
        self.var_word.set('')
        self.var_message.set('')
        self.words = []
        self.solution = None

    def shake(self):
        self.button_action.configure(text='Stop', command=self.solve)
        self.clear()
        self.letters = self.dice.shake()
        self.paint_canvas()
        self.running = True
        self.solution = self.solver.solve(self.letters)
        self.timer.start(180, self.solve)

    def add_word(self, event=None):
        word = self.var_word.get().strip()
        if self.running:
            if len(word) > 2 and word not in self.words:
                self.words.append(word)
                self.var_message.set('You entered:\n' + ' '.join(self.words))
        if word in self.solution:
            self.paint_canvas(self.solution[word])
        self.var_word.set('')
        self.root.after(2000, self.paint_canvas)

    def solve(self):
        if not self.running:
            return

        self.running = False
        self.button_action.configure(text='Shake!', command=self.shake)

        solution_words = set(self.solution.keys())
        entered_words = set(self.words)

        found = solution_words & entered_words
        missed = solution_words - entered_words

        found_score = self.score(found)
        found_words = ' '.join(sorted(list(found)))

        missed_score = self.score(missed)
        missed_words = ' '.join(sorted(list(missed)))

        if (missed_score + found_score) != 0:
            percent = (found_score / (found_score + missed_score)) * 100.0
        else:
            percent = 0.0

        self.var_message.set(
            'Your score %d (%d%%):\n%s\n\n' \
            'You missed %d:\n%s\n' % \
            (found_score, percent, found_words, missed_score, missed_words))

    def score(self, words):
        score = 0
        for word in words:
            score += self.points.get(len(word), 11)
        return score

def main():
    root = tk.Tk()
    BoggleApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
