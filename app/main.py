import os
import json
import tkinter as tk
from tkinter import messagebox

# Function to load driver data from a JSON file
def load_driver_data():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "driver-form")
    json_file = os.path.join(desktop_path, "drivers.json")

    if not os.path.exists(json_file):
        return []

    with open(json_file, "r") as file:
        return json.load(file)

# Function to create a box for each driver
def create_driver_box(parent, driver, show_driver_callback):
    box = tk.Frame(parent, borderwidth=2, relief="sunken", padx=5, pady=5)
    box.pack(fill="x", pady=5, expand=True)

    tk.Label(box, text=f"Name: {driver['name']}", font=("Arial", 14)).pack(side="left", padx=5)

    # Create and pack the show driver button
    show_driver_button = tk.Button(box, text="Show Details", command=lambda: show_driver_callback(driver))
    show_driver_button.pack(side="right", padx=5)

# Function to update the right frame with driver information
def show_driver_in_right_frame(driver):
    # Display all the driver details
    info_text = (
        f"Name: {driver['name']}\n"
        f"Car: {driver['car']['make']} {driver['car']['model']} ({driver['car']['year']})\n"
        f"License Number: {driver['license_number']}\n"
        f"State: {driver['state']}\n"
        f"License Expiration: {driver['license_expiration']}\n"
        f"Insurance Policy Number: {driver['insurance_policy_number']}\n"
        f"Insurance Expiration: {driver['insurance_expiration']}"
    )
    info_label.config(text=info_text)

def main():
    try:
        global info_label

        root = tk.Tk()
        root.title("Driver Car Inspection")
        root.geometry("800x500+400-200")

        # Create a PanedWindow with two sections
        paned_window = tk.PanedWindow(root, orient="horizontal")
        paned_window.pack(fill="both", expand=True)

        # Create the left section for driver entries
        left_frame = tk.Frame(paned_window, bg="lightgray")
        paned_window.add(left_frame, width=400, minsize=200)

        # Create the right section for displaying driver information
        right_frame = tk.Frame(paned_window, bg="white", padx=10, pady=10)
        paned_window.add(right_frame, width=400, minsize=200)

        # Add a canvas and scrollbar to the left frame
        canvas = tk.Canvas(left_frame, bg="lightgray")
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        driver_frame = tk.Frame(canvas, bg="lightgray")
        canvas.create_window((0, 0), window=driver_frame, anchor="nw")

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        driver_frame.bind("<Configure>", on_frame_configure)

        # Create a label to display driver information
        info_label = tk.Label(right_frame, text="Driver information will be shown here", font=("Arial", 16))
        info_label.pack(pady=20, anchor="w")

        drivers = load_driver_data()
        for driver in drivers:
            create_driver_box(driver_frame, driver, show_driver_in_right_frame)

        root.mainloop()
    except Exception as err:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", f"An error occurred: {err}")
        root.destroy()

if __name__ == "__main__":
    main()
