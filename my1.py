##

from tkinter import *
import time
import random

gameWidth = 500
gameHeight = 500
snakeItem = 10
snakeColor1 = "Red"
snakeColor2 = "Yellow"
snakeX = 24
snakeY = 24
snakeXnav = 0
snakeYnav = 0

snakeList = []
snakeSize = 3

virtual_game_x = gameWidth / snakeItem
virtual_game_y = gameHeight / snakeItem

tk = Tk()
tk.title("Игра змейка на Python")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=gameWidth, height=gameHeight, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

presentColor1 = "blue"
presentColor2 = "black"
presents_list = []
presents_size = 5
for i in range(presents_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x * snakeItem, y * snakeItem, x * snakeItem + snakeItem, y * snakeItem + snakeItem,
                             fill=presentColor2)
    id2 = canvas.create_oval(x * snakeItem + 2, y * snakeItem + 2, x * snakeItem + snakeItem - 2,
                             y * snakeItem + snakeItem - 2, fill=presentColor1)
    presents_list.append([x, y, id1, id2])
print(presents_list)


def snake_paint_items(canvas, x, y):
    global snakeList
    id1 = canvas.create_rectangle(x * snakeItem, y * snakeItem, x * snakeItem + snakeItem, y * snakeItem + snakeItem,
                                  fill=snakeColor2)
    id2 = canvas.create_rectangle(x * snakeItem + 2, y * snakeItem + 2, x * snakeItem + snakeItem - 2,
                                  y * snakeItem + snakeItem - 2, fill=snakeColor1)
    snakeList.append([x, y, id1, id2])
    print(snakeList)


snake_paint_items(canvas, snakeX, snakeY)


def check_can_we_delete_snake_item():
    if len(snakeList) >= snakeSize:
        temp_item = snakeList.pop(0)
        print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])

def check_if_we_found_present():
    global snakeSize
    for i in range(len(presents_list)):

    [snakeX, snakeY]

def snake_move(event):
    global snakeX
    global snakeY
    if event.keysym == "Up":
        snakeXnav = 0
        snakeYnav = -1
        check_can_we_delete_snake_item()
    elif event.keysym == "Down":
        snakeXnav = 0
        snakeYnav = 1
        check_can_we_delete_snake_item()
    elif event.keysym == "Left":
        snakeXnav = -1
        snakeYnav = 0
        check_can_we_delete_snake_item()
    elif event.keysym == "Right":
        snakeXnav = 1
        snakeYnav = 0
        check_can_we_delete_snake_item()
    snakeX = snakeX + snakeXnav
    snakeY = snakeY + snakeYnav
    snake_paint_items(canvas, snakeX, snakeY)
    check_if_we_found_present()


canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)
