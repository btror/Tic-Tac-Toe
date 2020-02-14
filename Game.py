from tkinter import *

tk = Tk()
tk.title("Tic-Tac-Toe GUI")
tk.geometry("425x425")
tk.resizable(False, False)

buttonList = []
isClicked = True


def buttonClicked(button):
    global isClicked

    if button['text'] == "" and isClicked == True:
        button.config(text="X")
        isClicked = False
    elif button['text'] == "" and isClicked == False:
        button['text'] = "O"
        isClicked = True

    winnerIcon = button['text']
    winnerPresent = False
    # check for a winner
    if buttonList[0]['text'] == buttonList[1]['text'] == buttonList[2]['text'] and len(
            buttonList[0]['text']) != 0 and len(buttonList[1]['text']) != 0 and len(buttonList[2]['text']) != 0:
        winnerPresent = True
    if buttonList[0]['text'] == buttonList[4]['text'] == buttonList[8]['text'] and len(
            buttonList[0]['text']) != 0 and len(buttonList[4]['text']) != 0 and len(buttonList[8]['text']) != 0:
        winnerPresent = True
    if buttonList[0]['text'] == buttonList[3]['text'] == buttonList[6]['text'] and len(
            buttonList[0]['text']) != 0 and len(buttonList[3]['text']) != 0 and len(buttonList[6]['text']) != 0:
        winnerPresent = True
    if buttonList[1]['text'] == buttonList[4]['text'] == buttonList[7]['text'] and len(
            buttonList[1]['text']) != 0 and len(buttonList[4]['text']) != 0 and len(buttonList[7]['text']) != 0:
        winnerPresent = True
    if buttonList[2]['text'] == buttonList[5]['text'] == buttonList[8]['text'] and len(
            buttonList[2]['text']) != 0 and len(buttonList[5]['text']) != 0 and len(buttonList[8]['text']) != 0:
        winnerPresent = True
    if buttonList[2]['text'] == buttonList[4]['text'] == buttonList[6]['text'] and len(
            buttonList[2]['text']) != 0 and len(buttonList[4]['text']) != 0 and len(buttonList[6]['text']) != 0:
        winnerPresent = True
    if buttonList[3]['text'] == buttonList[4]['text'] == buttonList[5]['text'] and len(
            buttonList[3]['text']) != 0 and len(buttonList[4]['text']) != 0 and len(buttonList[5]['text']) != 0:
        winnerPresent = True
    if buttonList[6]['text'] == buttonList[7]['text'] == buttonList[8]['text'] and len(
            buttonList[6]['text']) != 0 and len(buttonList[7]['text']) != 0 and len(buttonList[8]['text']) != 0:
        winnerPresent = True

    # if a winner is present show a popup window
    if winnerPresent:
        popup = Tk()
        popup.resizable(False, False)
        popup.title("Game Over")
        popup.geometry("300x300")
        msg = winnerIcon + " wins!"
        label = Label(popup, text=msg, width=120, height=10, font=('Helvetica', '25'))
        label.pack()
        for x in buttonList:
            x['text'] = ''


for i in range(9):
    buttonList.append(Button(bg='white', fg='black', height=3, width=7, font=('Helvetica', '25')))

row = 1
column = 0
index = 1
buttons = StringVar()

for i in buttonList:
    i.grid(row=row, column=column, sticky=NSEW)
    i.config(command=lambda button=i: buttonClicked(button))
    column += 1
    if index % 3 == 0:
        row += 1
        column = 0
    index += 1

tk.mainloop()