import tkinter
import model

CELL_SIZE = 5


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
    start_button.grid(row=1, column=0, sticky='W', padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky='E', padx=20, pady=20)


if __name__ == "__main__":
    setup()
    tkinter.mainloop()
