import tkinter as tk

# The initial stock of propellers
prop_stock = {
    "5inch": {
        "5043": 50,

    },
    "7inch": {
        "51477": 20,

    }
}

# The main window
root = tk.Tk()
root.title("Propeller Stock Management")

# The counter for the total amount of props in stock
total_props = sum([sum(values.values()) for values in prop_stock.values()])
counter_label = tk.Label(root, text=f"Total Props in Stock: {total_props}")
counter_label.pack()

# The input propeller frame
input_frame = tk.Frame(root)
input_frame.pack(side="left", padx=10, pady=10)

input_label = tk.Label(input_frame, text="Input Propeller")
input_label.pack()

size_label = tk.Label(input_frame, text="Size:")
size_label.pack()

size_var = tk.StringVar(value="5inch")
size_entry = tk.Entry(input_frame, textvariable=size_var)
size_entry.pack()

prop_label = tk.Label(input_frame, text="Propeller:")
prop_label.pack()

prop_var = tk.StringVar(value="5043")
prop_entry = tk.Entry(input_frame, textvariable=prop_var)
prop_entry.pack()

quantity_label = tk.Label(input_frame, text="Quantity:")
quantity_label.pack()

quantity_var = tk.StringVar(value="1")
quantity_entry = tk.Entry(input_frame, textvariable=quantity_var)
quantity_entry.pack()

def add_prop():
    size = size_var.get()
    prop = prop_var.get()
    quantity = int(quantity_var.get())
    if size in prop_stock and prop in prop_stock[size]:
        prop_stock[size][prop] += quantity
    else:
        prop_stock[size][prop] = quantity
    total_props = sum([sum(values.values()) for values in prop_stock.values()])
    counter_label.config(text=f"Total Props in Stock: {total_props}")

add_button = tk.Button(input_frame, text="Add Propeller", command=add_prop)
add_button.pack()


root.mainloop()
