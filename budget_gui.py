import tkinter as tk
from tkinter import messagebox


items = []


def add_item():
    name = name_entry.get()
    try:
        cost = float(cost_entry.get())
        value = float(value_entry.get())

        if cost <= 0 or value <= 0:
            raise ValueError

        items.append({"name": name, "cost": cost, "value": value})

        listbox.insert(tk.END, f"{name} | Cost: {cost} | Value: {value}")

        name_entry.delete(0, tk.END)
        cost_entry.delete(0, tk.END)
        value_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Enter valid positive numbers!")


def optimize():
    try:
        budget = float(budget_entry.get())
        if budget <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid budget!")
        return

    sorted_items = sorted(items, key=lambda x: x["value"] / x["cost"], reverse=True)

    total_value = 0
    result = "Selected Items:\n\n"

    remaining = budget

    for item in sorted_items:
        if remaining == 0:
            break

        if item["cost"] <= remaining:
            result += f"✔ {item['name']} (Full)\n"
            remaining -= item["cost"]
            total_value += item["value"]
        else:
            fraction = remaining / item["cost"]
            result += f"✔ {item['name']} ({round(fraction*100,2)}%)\n"
            total_value += item["value"] * fraction
            remaining = 0

    result += f"\nTotal Value: {round(total_value,2)}"
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)



root = tk.Tk()
root.title("Budget Optimizer (Fractional Knapsack)")
root.geometry("500x600")


tk.Label(root, text="Item Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Cost").pack()
cost_entry = tk.Entry(root)
cost_entry.pack()

tk.Label(root, text="Value").pack()
value_entry = tk.Entry(root)
value_entry.pack()

tk.Button(root, text="Add Item", command=add_item).pack(pady=5)


listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

tk.Label(root, text="Enter Budget").pack()
budget_entry = tk.Entry(root)
budget_entry.pack()

tk.Button(root, text="Optimize", command=optimize).pack(pady=10)


result_box = tk.Text(root, height=10, width=50)
result_box.pack(pady=10)


root.mainloop()
