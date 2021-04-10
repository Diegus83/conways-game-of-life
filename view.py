import tkinter
import model

CELL_SIZE = 5
IS_RUNNING = False


def setup():
    global root, grid_view, CELL_SIZE, start_button, clear_button, choice

    root = tkinter.Tk()
    root.title("Conway's Game of Life")

    grid_view = tkinter.Canvas(
        root,
        width=model.WIDTH * CELL_SIZE,
        height=model.HEIGHT * CELL_SIZE,
        borderwidth=0,
        highlightthickness=0,
        bg="white",
    )

    start_button = tkinter.Button(root, text="Start", width=12)
    clear_button = tkinter.Button(root, text="Clear", width=12)

    choice = tkinter.StringVar(root)
    choice.set("Choose a Pattern")
    option = tkinter.OptionMenu(
        root, choice, "Choose a Pattern", "glider", "glider gun", "random"
    )
    option.config(width=20)

    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    start_button.grid(row=1, column=0, sticky='w', padx=20, pady=20)
    start_button.bind('<Button-1>', start_handler)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky='e', padx=20, pady=20)
    clear_button.bind('<Button-1>', clear_handler)

def start_handler(event):
    global IS_RUNNING, start_button

    if IS_RUNNING:
        IS_RUNNING = False
        start_button.configure(text='Start')
    else:
        IS_RUNNING = True
        start_button.configure(text='Pause')
        update()

def clear_handler(event):
    global IS_RUNNING, start_button

    IS_RUNNING = False
    for i in range(0, model.HEIGHT):
        for j in range(0, model.WIDTH):
            model.GRID_MODEL[i][j] = 0

    start_button.configure(text='Start')
    update()

def update():
    global grid_view, root, IS_RUNNING

    grid_view.delete('all')

    model.next_gen()
    for i in range(0, model.HEIGHT):
        for j in range(0, model.WIDTH):
            if model.GRID_MODEL[i][j] == 1:
                draw_cell(i, j, "black")

    if IS_RUNNING:
        root.after(100, update)


def draw_cell(row, col, color):
    global grid_view, CELL_SIZE
    if color == "black":
        outline = "grey"
    else:
        outline = "white"

    grid_view.create_rectangle(
        row * CELL_SIZE,
        col * CELL_SIZE,
        row * CELL_SIZE + CELL_SIZE,
        col * CELL_SIZE + CELL_SIZE,
        fill=color,
        outline=outline,
    )


if __name__ == "__main__":
    setup()
    model.randomize(model.GRID_MODEL, model.WIDTH, model.HEIGHT)
    update()
    tkinter.mainloop()
