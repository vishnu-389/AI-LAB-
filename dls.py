'''import tkinter as tk

# Create window
root = tk.Tk()
root.title("Water Tank Control")
root.geometry("700x700")
root.resizable(False, False)

# Maximum capacity
MAX_CAPACITY = 100

# Take input from user
amount = float(input("Enter water level (0-100 ml): "))

# Check input
if amount < 0 or amount > MAX_CAPACITY:
    print("Please enter a value between 0 and 100 ml.")
    root.destroy()
    exit()

# Calculate percentage
percentage = (amount / MAX_CAPACITY) * 100
remaining = MAX_CAPACITY - amount

# Canvas
canvas = tk.Canvas(
    root,
    width=700,
    height=700,
    bg="black"
)
canvas.pack()

# --------------------------------
# TITLE
# --------------------------------

canvas.create_text(
    350, 35,
    text="WATER TANK CONTROL",
    font=("Arial", 24, "bold"),
    fill="white"
)

canvas.create_text(
    350, 70,
    text="Maximum Tank Capacity = 100 ml",
    font=("Arial", 16, "bold"),
    fill="white"
)

# --------------------------------
# TANK DIMENSIONS
# --------------------------------

left = 220
right = 520
top = 130
bottom = 550

tank_height = bottom - top

# --------------------------------
# TANK OUTLINE
# --------------------------------

canvas.create_rectangle(
    left,
    top,
    right,
    bottom,
    outline="white",
    fill="black",
    width=5
)

# --------------------------------
# WATER LEVEL
# --------------------------------

water_height = tank_height * (amount / MAX_CAPACITY)

water_top = bottom - water_height

# Water
canvas.create_rectangle(
    left + 5,
    water_top,
    right - 5,
    bottom - 5,
    fill="skyblue",
    outline="blue",
    width=2
)

# Water surface
canvas.create_oval(
    left + 5,
    water_top - 7,
    right - 5,
    water_top + 7,
    fill="skyblue",
    outline="blue"
)

# --------------------------------
# MEASUREMENT SCALE
# --------------------------------

scale_x = left - 20

for ml in range(0, 101, 20):

    y = bottom - (tank_height * ml / MAX_CAPACITY)

    # Scale line
    canvas.create_line(
        scale_x,
        y,
        left,
        y,
        fill="white",
        width=3
    )

    # Scale label
    canvas.create_text(
        scale_x - 15,
        y,
        text=f"{ml} ml",
        font=("Arial", 13, "bold"),
        fill="white",
        anchor="e"
    )

# --------------------------------
# CURRENT WATER LEVEL
# --------------------------------

canvas.create_text(
    370,
    water_top + 80,
    text=f"{amount:g} ml",
    font=("Arial", 24, "bold"),
    fill="white"
)

canvas.create_text(
    370,
    water_top + 115,
    text="CURRENT WATER LEVEL",
    font=("Arial", 13),
    fill="white"
)

# --------------------------------
# TANK CONTROL INFORMATION
# --------------------------------

canvas.create_text(
    350,
    590,
    text=f"Tank Level: {percentage:.0f}%",
    font=("Arial", 16, "bold"),
    fill="white"
)

canvas.create_text(
    350,
    620,
    text=f"Water Available: {amount:g} ml",
    font=("Arial", 15),
    fill="white"
)

canvas.create_text(
    350,
    650,
    text=f"Available Space: {remaining:g} ml",
    font=("Arial", 15),
    fill="white"
)

# --------------------------------
# RUN
# --------------------------------

root.mainloop()
'''




import tkinter as tk

# --------------------------------
# CONSTANTS
# --------------------------------
MAX_CAPACITY = 100

# --------------------------------
# CREATE WINDOW
# --------------------------------
root = tk.Tk()
root.title("Water Tank Control")
root.geometry("750x780")
root.resizable(False, False)

# --------------------------------
# CANVAS
# --------------------------------
canvas = tk.Canvas(
    root,
    width=750,
    height=780,
    bg="white",
    highlightthickness=0
)
canvas.pack()

# --------------------------------
# TITLE
# --------------------------------
canvas.create_text(
    375, 35,
    text="WATER TANK CONTROL",
    font=("Arial", 26, "bold"),
    fill="black"
)

canvas.create_text(
    375, 70,
    text="Smart Water Level Monitoring System",
    font=("Arial", 15),
    fill="gray"
)

# --------------------------------
# INPUT
# --------------------------------
canvas.create_text(
    260, 110,
    text="Enter Water Level (0-100 ml):",
    font=("Arial", 14, "bold"),
    fill="black"
)

entry = tk.Entry(
    root,
    font=("Arial", 14, "bold"),
    width=10,
    justify="center",
    bg="white",
    fg="black",
    relief="solid",
    bd=2
)

entry.place(x=480, y=95)

# --------------------------------
# TANK DIMENSIONS
# --------------------------------
left = 240
right = 570
top = 160
bottom = 590

tank_height = bottom - top

# --------------------------------
# TANK OUTER BODY
# --------------------------------
canvas.create_rectangle(
    left - 12,
    top - 12,
    right + 12,
    bottom + 12,
    fill="white",
    outline="black",
    width=5
)

# Main tank
canvas.create_rectangle(
    left,
    top,
    right,
    bottom,
    fill="white",
    outline="black",
    width=4
)

# --------------------------------
# TANK TOP
# --------------------------------
canvas.create_rectangle(
    left - 10,
    top - 25,
    right + 10,
    top,
    fill="white",
    outline="black",
    width=4
)

# Tank handle
canvas.create_rectangle(
    left + 110,
    top - 48,
    right - 110,
    top - 25,
    fill="white",
    outline="black",
    width=4
)

# --------------------------------
# TANK BOTTOM / SUPPORT
# --------------------------------
canvas.create_line(
    left - 15,
    bottom + 15,
    left + 45,
    bottom + 15,
    fill="black",
    width=6
)

canvas.create_line(
    right - 45,
    bottom + 15,
    right + 15,
    bottom + 15,
    fill="black",
    width=6
)

# --------------------------------
# MEASUREMENT SCALE
# --------------------------------
scale_x = left - 30

for ml in range(0, 101, 20):

    y = bottom - (
        tank_height * ml / MAX_CAPACITY
    )

    # Scale line
    canvas.create_line(
        scale_x,
        y,
        left,
        y,
        fill="black",
        width=3
    )

    # Scale label
    canvas.create_text(
        scale_x - 15,
        y,
        text=f"{ml} ml",
        font=("Arial", 13, "bold"),
        fill="black",
        anchor="e"
    )

# --------------------------------
# WATER VARIABLES
# --------------------------------
current_amount = 0
target_amount = 0

water = None
water_surface = None

amount_text = None
tank_level_text = None


# --------------------------------
# UPDATE WATER
# --------------------------------
def update_water():

    global current_amount
    global water
    global water_surface

    # Calculate water height
    water_height = (
        tank_height *
        current_amount /
        MAX_CAPACITY
    )

    water_top = bottom - water_height

    # Delete old water
    if water is not None:
        canvas.delete(water)

    if water_surface is not None:
        canvas.delete(water_surface)

    # Draw water
    if current_amount > 0:

        water = canvas.create_rectangle(
            left + 5,
            water_top,
            right - 5,
            bottom - 5,
            fill="skyblue",
            outline="blue",
            width=2
        )

        # Water surface
        water_surface = canvas.create_oval(
            left + 5,
            water_top - 8,
            right - 5,
            water_top + 8,
            fill="skyblue",
            outline="blue",
            width=2
        )

    # Current amount
    canvas.itemconfig(
        amount_text,
        text=f"{current_amount} ml"
    )

    # Percentage
    percentage = (
        current_amount /
        MAX_CAPACITY
    ) * 100

    canvas.itemconfig(
        tank_level_text,
        text=f"Tank Level: {percentage:.0f}%"
    )

    # Continue filling
    if current_amount < target_amount:

        current_amount += 1

        root.after(
            40,
            update_water
        )

    else:

        status_label.config(
            text="Tank Filled Successfully!",
            fg="green"
        )


# --------------------------------
# START FILLING
# --------------------------------
def start_filling():

    global target_amount
    global current_amount

    try:

        target_amount = int(entry.get())

        if target_amount < 0 or target_amount > 100:

            status_label.config(
                text="Enter a value between 0 and 100 ml!",
                fg="red"
            )

            return

    except ValueError:

        status_label.config(
            text="Please enter a valid number!",
            fg="red"
        )

        return

    # Start from 0 ml
    current_amount = 0

    status_label.config(
        text="Filling Tank...",
        fg="blue"
    )

    update_water()


# --------------------------------
# BUTTON
# --------------------------------
button = tk.Button(
    root,
    text="FILL TANK",
    font=("Arial", 13, "bold"),
    command=start_filling,
    bg="black",
    fg="white",
    width=14,
    height=2,
    cursor="hand2"
)

button.place(
    x=305,
    y=705
)

# --------------------------------
# CURRENT AMOUNT
# --------------------------------
amount_text = canvas.create_text(
    405,
    350,
    text="0 ml",
    font=("Arial", 30, "bold"),
    fill="black"
)

# --------------------------------
# TANK LEVEL
# --------------------------------
tank_level_text = canvas.create_text(
    405,
    390,
    text="Tank Level: 0%",
    font=("Arial", 16, "bold"),
    fill="black"
)

# --------------------------------
# STATUS MESSAGE
# --------------------------------
status_label = tk.Label(
    root,
    text="Enter amount and click FILL TANK",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="black"
)

status_label.place(
    x=255,
    y=670
)

# --------------------------------
# RUN PROGRAM
# --------------------------------
root.mainloop()