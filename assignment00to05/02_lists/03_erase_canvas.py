import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse info to help us know which cells to delete
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()

    # Calculate where our eraser is
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Find things that overlap with our eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    # For everything that overlaps with our eraser (that isn't our eraser), change
    # its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.itemconfig(overlapping_object, fill='white')

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # Figure out how many columns of cells we need

    # Make a grid of squares based on the number of rows and columns.
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            # Create a single cell in the grid
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')

    def on_click(event):
        nonlocal eraser
        # Create our eraser
        eraser = canvas.create_rectangle(
            event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill='pink'
        )
        canvas.bind('<Motion>', on_motion)

    def on_motion(event):
        # Move the eraser, and erase what it's touching
        canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        erase_objects(canvas, eraser)

    eraser = None
    canvas.bind('<Button-1>', on_click)

    root.mainloop()

if __name__ == '__main__':
    main()
