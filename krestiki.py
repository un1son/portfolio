import tkinter
from tkinter.messagebox import showinfo
import random

colors = ['#FF00FF','#BA55D3','#0000FF','#7B68EE','#F4A460']

root = tkinter.Tk()
root.title('Крестики-нолики')
#root.geometry('600x500')

player = 'x'

buttons = []
for i in range(3):
    b = []
    for j in range(3):
        b.append(None)
    buttons.append(b)


def on_button_click(row, col):
    global player
    print(check_d())
    buttons[row][col]['background'] = colors[random.randint(0, len(colors) - 1)]

    if buttons[row][col]['text'] == '' and not check_winner():
        buttons[row][col]['text'] = player
        if check_winner():
            showinfo('Победа!', f"Игрок {player} победил")
            reset_game()
        elif check_d():

            showinfo('Ничья!', f"Ничья")
            reset_game()
        else:
            if player == 'x':
                player = '0'
            else:
                player = 'x'


def check_d():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == '':
                return False

    return True

def reset_game():
    global player
    global buttons
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
            buttons[row][col]['background'] = '#0f0'
    player = 'x'


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != '':
            return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True

    return False



for row in range(3):
    for col in range(3):
        button = tkinter.Button(text='',font=('Arial', 40), width=5, height=2,background='#0f0', command=lambda r=row,c=col: on_button_click(r,c))
        button.grid(row=row, column=col)
        buttons[row][col] = button
root.mainloop()
