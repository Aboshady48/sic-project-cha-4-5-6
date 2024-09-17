import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item['price'] for item in self.items)

    def calculate_delivery_fee(self, governorate):
        return 50 if governorate != 'Cairo' else 0

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart")
        self.cart = Cart()
        self.create_widgets()

    def create_widgets(self):
        # Main frame the page
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(pady=10)

        # Add to Cart button on the main page
        self.add_to_cart_main_button = ttk.Button(self.main_frame, text="Add to Cart", command=self.show_add_to_cart_page)
        self.add_to_cart_main_button.pack(pady=10)

        # Cart frame (hidden initially)
        self.cart_frame = ttk.Frame(self.root)
        self.cart_listbox = tk.Listbox(self.cart_frame, height=10, width=70)
        self.cart_listbox.pack(side=tk.LEFT, padx=10)

        self.cart_scrollbar = tk.Scrollbar(self.cart_frame, orient=tk.VERTICAL, command=self.cart_listbox.yview)
        self.cart_scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.cart_listbox.config(yscrollcommand=self.cart_scrollbar.set)

        self.add_to_cart_button = ttk.Button(self.cart_frame, text="Add Item to Cart", command=self.add_item_to_cart)
        self.add_to_cart_button.pack(pady=10)

        self.view_cart_button = ttk.Button(self.cart_frame, text="View Cart", command=self.view_cart)
        self.view_cart_button.pack(pady=10)

        self.calculate_total_button = ttk.Button(self.cart_frame, text="Calculate Total Cost", command=self.calculate_cart_total)
        self.calculate_total_button.pack(pady=10)

        self.calculate_delivery_fee_button = ttk.Button(self.cart_frame, text="Calculate Delivery Fee", command=self.calculate_delivery_fee)
        self.calculate_delivery_fee_button.pack(pady=10)

    def show_add_to_cart_page(self):
        self.main_frame.pack_forget()
        self.cart_frame.pack(pady=10)

    def add_item_to_cart(self):
        item_name = simpledialog.askstring("Input", "Enter item name to add to cart:")
        item_price = simpledialog.askfloat("Input", "Enter item price:")
        if item_name and item_price is not None:
            item = {'name': item_name, 'price': item_price}
            self.cart.add_item(item)
            messagebox.showinfo("Add to Cart", f"Added '{item_name}' to cart.")
            self.update_cart_listbox()

    def view_cart(self):
        items = "\n".join([f"{item['name']}: ${item['price']}" for item in self.cart.items])
        messagebox.showinfo("Cart Items", f"Items in cart:\n{items}")

    def calculate_cart_total(self):
        total = self.cart.calculate_total()
        messagebox.showinfo("Total Cost", f"Total cost: ${total}")

    def calculate_delivery_fee(self):
        governorate = simpledialog.askstring("Input", "Enter your governorate:")
        fee = self.cart.calculate_delivery_fee(governorate)
        messagebox.showinfo("Delivery Fee", f"Delivery fee: ${fee}")

    def update_cart_listbox(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart.items:
            self.cart_listbox.insert(tk.END, f"{item['name']}: ${item['price']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()