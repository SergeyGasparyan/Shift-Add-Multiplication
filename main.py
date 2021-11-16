from tkinter import *
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        # Inheritance
        super().__init__()
        # Initial setup for window
        self.geometry('355x320')
        self.title("Add shift multiplication method")
        self['bg'] = 'white'
        # Attributes
        self.frm = None
        self.lbl_1, self.lbl_2 = None, None
        self.ent_1, self.ent_2 = None, None
        self.btn_1, self.btn_2 = None, None
        # for step by step execution
        self.carry_for_shift = False
        self.m, self.c, self.a, self.q, self.op = 0, 0, 0, 0, 'Init'
        self.row = 2
        self.x, self.y = 0, 0
        self.cycle = 1
        # Initialize values
        self.restart_game()

    def step_1(self):
        self.carry_for_shift = False
        self.m, self.c, self.a, self.q, self.op = self.x, 0, 0, self.y, 'Init'

        self.show_text(self.row, f'   M|C|   A|   Q|Operation')
        self.row += 1

        self.show_text(
            self.row,
            f'{bin(self.m)[2:].zfill(4)}|{self.c}|{bin(self.a)[2:].zfill(4)}|{bin(self.q)[2:].zfill(4)}|{self.op}'
        )
        self.row += 1

        btn = Button(self, text='Step', bg='orange', command=self.step_2)
        btn.place(x=262, y=5)

    def step_2(self):
        if bin(self.q)[-1] == '1':
            self.op = f'{self.cycle} cycle: Add'
            self.a += self.m
            if len(bin(self.a)[2:]) > 4:
                self.c = 1
                self.a -= 16
            self.show_text(self.row, f'    |{self.c}|{bin(self.a)[2:].zfill(4)}|{bin(self.q)[2:].zfill(4)}|{self.op}')
            self.row += 1

        self.op = f'{self.cycle} cycle: Shift'
        if bin(self.a)[-1] == '1':
            self.carry_for_shift = True
        self.a = self.a >> 1
        self.a += self.c * 8
        self.c = 0
        self.q = self.q >> 1
        self.q += self.carry_for_shift * 8
        self.carry_for_shift = False

        self.show_text(self.row, f'    |{self.c}|{bin(self.a)[2:].zfill(4)}|{bin(self.q)[2:].zfill(4)}|{self.op}')
        self.row += 1

        self.cycle += 1
        if self.cycle != 5:
            btn = Button(self, text='Step', bg='orange', command=self.step_2)
            btn.place(x=262, y=5)
        else:
            ans = '0b' + bin(self.a)[2:].zfill(4) + bin(self.q)[2:].zfill(4)
            ans = int(ans, 2)

            lbl = Label(self.frm, text=f'Answer is {ans}')
            lbl.grid(row=self.row, column=6)

            btn = Button(self, text='Restart', bg='orange', command=self.restart_game)
            btn.place(x=252, y=30)

    def restart_game(self):
        self.carry_for_shift = False
        self.m, self.c, self.a, self.q, self.op = 0, 0, 0, 0, 'Init'
        self.row = 2
        self.cycle = 1
        self.x, self.y = 0, 0
        if self.frm is not None:
            self.frm.destroy()
        self.frm = Frame(self, relief=GROOVE, bd=1)
        self.frm.place(x=10, y=85)
        self.lbl_1 = Label(self, text='Enter A')
        self.lbl_1.place(x=0, y=10)
        self.lbl_2 = Label(self, text='Enter B')
        self.lbl_2.place(x=0, y=35)
        self.ent_1 = Entry(self, bd=5)
        self.ent_1.place(x=53, y=5)
        self.ent_2 = Entry(self, bd=5)
        self.ent_2.place(x=53, y=30)
        self.btn_1 = Button(self, text='Start  ', bg='blue', command=self.start)
        self.btn_1.place(x=257, y=5)
        self.btn_2 = Button(self, text='By step', bg='red', command=self.by_step)
        self.btn_2.place(x=252, y=30)

    def init_values(self):
        self.x = self.ent_1.get()
        self.y = self.ent_2.get()
        self.x, self.y = int(self.x), int(self.y)

    def start(self):
        self.init_values()
        if self.x > 15 or self.y > 15:
            messagebox.showwarning('Warning', 'Enter numbers that are less than 16!')
            self.restart_game()
        else:
            self.add_shift_multiply_method()

    def by_step(self):
        self.init_values()
        if self.x > 15 or self.y > 15:
            messagebox.showwarning('Warning', 'Enter numbers that are less than 16!')
            self.restart_game()
        else:
            self.btn_1.destroy()
            self.btn_2.destroy()
            btn = Button(self, text='Step', bg='orange', command=self.step_1)
            btn.place(x=262, y=5)

    def show_text(self, row, text):
        column = 0
        for txt in text.split('|'):
            lbl = Label(self.frm, text=txt)
            lbl.grid(row=row, column=column)
            column += 1

            lbl = Label(self.frm, text='|')
            lbl.grid(row=row, column=column)
            column += 1

    def add_shift_multiply_method(self):
        carry_for_shift = False
        m, c, a, q, op = self.x, 0, 0, self.y, 'Init'
        row = 2

        self.show_text(row, f'   M|C|   A|   Q|Operation')
        row += 1

        self.show_text(row, f'{bin(m)[2:].zfill(4)}|{c}|{bin(a)[2:].zfill(4)}|{bin(q)[2:].zfill(4)}|{op}')
        row += 1

        for cycle in range(1, 5):
            if bin(q)[-1] == '1':
                op = f'{cycle} cycle: Add'
                a += m
                if len(bin(a)[2:]) > 4:
                    c = 1
                    a -= 16
                self.show_text(row, f'    |{c}|{bin(a)[2:].zfill(4)}|{bin(q)[2:].zfill(4)}|{op}')
                row += 1

            op = f'{cycle} cycle: Shift'
            if bin(a)[-1] == '1':
                carry_for_shift = True
            a = a >> 1
            a += c * 8
            c = 0
            q = q >> 1
            q += carry_for_shift * 8
            carry_for_shift = False

            self.show_text(row, f'    |{c}|{bin(a)[2:].zfill(4)}|{bin(q)[2:].zfill(4)}|{op}')
            row += 1

        ans = '0b' + bin(a)[2:].zfill(4) + bin(q)[2:].zfill(4)
        ans = int(ans, 2)

        lbl = Label(self.frm, text=f'Answer is {ans}')
        lbl.grid(row=row, column=6)

        btn = Button(self, text='Restart', bg='orange', command=self.restart_game)
        btn.place(x=252, y=30)


if __name__ == '__main__':
    App().mainloop()
