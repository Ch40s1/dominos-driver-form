import tkinter as tk
from tkinter import Canvas, ttk, messagebox


# Define main function to initialize and run the application
def main():
    try:
        # creates main application window
        root = tk.Tk()
        # sets the title of the main window
        root.title("Driver Car Inspection")
        # sets siz 800px by 500px with a screen displacement of 400 x
        # and 200 y from the top left 0,0
        root.geometry("800x500+400-200")

        # Create the main content frame widget
        # within the main window(root) with a 5 px border and a ridge relief(3d appearance)
        content = tk.Frame(root, borderwidth=5, relief="ridge")
        # content frame uses grid and places it in column 0, row 0
        # exapnds in all directions (north, south, east, west)
        content.grid(column=0, row=0, sticky="nsew")

        # Configure the grid layout
        # ensures that the content frame and its child widgets can expand to fill the available space
        #################################
        # Allows the single cell in the root window (column 0, row 0) to expand when the window is resized
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        ################################
        # configures the columns and rows in the content frame to expand proportionally.
        # each column gains a weight of 1 meaning they will expand equally
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        content.columnconfigure(2, weight=1)
        content.rowconfigure(1, weight=1)

        # Create buttons create, delete, search,
        create_button = tk.Button(content, text="Create")
        delete_button = tk.Button(content, text="Delete")
        search_button = tk.Button(content, text="Search")

        # places button on top row
        # sticky 'ew' makes the button expand horizontally
        create_button.grid(column=0, row=0, sticky="ew")
        delete_button.grid(column=1, row=0, sticky="ew")
        search_button.grid(column=2, row=0, sticky="ew")

        # Create a main canvas within content frame, border 2px, background white, sunken relief(indented appearance)
        # places the canvas in row 1 col 0, and expands all directions
        canvas = tk.Canvas(content, borderwidth=2, relief="sunken", bg="white")
        canvas.grid(column=0, row=1, columnspan=2, rowspan=2, sticky="nsew")

        # Create empty area (right side)
        news_area = tk.Frame(content, borderwidth=2, relief="sunken")
        news_area.grid(column=2, row=1, rowspan=2, sticky="nsew")

        root.mainloop()
    except Exception as err:
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showerror("Error", f"An error occurred: {err}")
        root.destroy()
#  Ensures that the main() function is called only when the script is run directly, not when it is imported as a module.
if __name__ == "__main__":
    main()
