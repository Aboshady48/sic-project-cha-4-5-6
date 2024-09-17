import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class Item:
    def __init__(self, name, price, brand, model_year, id, color):
        self.name = name
        self.price = price
        self.brand = brand
        self.model_year = model_year
        self.id = id
        self.color = color



class Category:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def calculate_delivery_fee(self, governorate):
        return 50 if governorate != 'Cairo' else 0


categories = {name: Category(name) for name in ['Home Appliances', 'Electronics', 'Fashion', 'Books', 'Sports']}
cart = Cart()

class User:
    def __init__(self, gmail, user_id):
        self.gmail = gmail
        self.id = user_id

    def navg(self):
        return self.id

    def add_to_cart(self, item):
        return item

class Admin:
    def __init__(self, admin_id):
        self.admin_id = admin_id

    def add_item_to_app(self, item):
        return item

    def remove_item(self, item_id):
        return item_id

class Member(Admin, User):
    def __init__(self, admin_id, user_id, gmail):
        User.__init__(self, gmail, user_id)
        Admin.__init__(self, admin_id)

#gui
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Member")
        self.member = Member("mo_aboshady", "aboshady22", "aboshady@egmail.com")
        self.create_widgets()

    def create_widgets(self):
        self.tab_control = ttk.Notebook(self.root)

        self.tab_categories = ttk.Frame(self.tab_control)
        self.tab_cart = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_categories, text='Categories')
        self.tab_control.pack(expand=1, fill='both')

# categories Tab
        self.category_frame = ttk.Frame(self.tab_categories)
        self.category_frame.pack(pady=10)

        self.category_listbox = tk.Listbox(self.category_frame, height=10, width=50)
        self.category_listbox.pack(side=tk.LEFT, padx=10)

        self.category_scrollbar = tk.Scrollbar(self.category_frame, orient=tk.VERTICAL, command=self.category_listbox.yview)
        self.category_scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.category_listbox.config(yscrollcommand=self.category_scrollbar.set)

        self.add_item_button = ttk.Button(self.tab_categories, text="Add Item to Category", command=self.add_item_to_category)
        self.add_item_button.pack(pady=10)

        self.view_items_button = ttk.Button(self.tab_categories, text="View Items in Category", command=self.view_items_in_category)
        self.view_items_button.pack(pady=10)
        
        self.view_items_button = ttk.Button(self.tab_categories, text="Add This item in Cart", command=self.add_to_cart)
        self.view_items_button.pack(pady=10)
        
        
        self.view_items_button = ttk.Button(self.tab_categories, text="Show Your Cart item", command=self.show_add_to_cart_page)
        self.view_items_button.pack(pady=10)
        
        #sort categouries
        #self.sort_categories_by_price()

# cart Tab# Main frame the page
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(pady=120)

        # Add to Cart button on the main page
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

        self.update_category_listbox()

    def navigate(self):
        user_id = self.member.navg()
        messagebox.showinfo("Navigate", f"User ID: {user_id}")

    def add_to_cart(self):
        item = simpledialog.askstring("Input", "Enter item name to add to cart:")
        if item:
            self.member.add_to_cart(item)
            messagebox.showinfo("Add to Cart", f"Added '{item}' to cart.")
            

    def show_add_to_cart_page(self):
        self.main_frame.pack_forget()
        self.cart_frame.pack(pady=10)


    def add_item(self):
        item_name = simpledialog.askstring("Input", "Enter item name to add:")
        if item_name:
            self.member.add_item_to_app(item_name)
            messagebox.showinfo("Add Item", f"Added '{item_name}' to app.")

    def remove_items(self):
        item_id = simpledialog.askstring("Input", "Enter item ID to remove:")
        if item_id:
            self.member.remove_item(item_id)
            messagebox.showinfo("Remove Item", f"Removed item with ID '{item_id}'.")

    def update_category_listbox(self):
        self.category_listbox.delete(0, tk.END)
        for name in categories:
            self.category_listbox.insert(tk.END, name)

    def add_item_to_category(self):
        category_name = self.category_listbox.get(tk.ACTIVE)
        if not category_name:
            messagebox.showwarning("Selection Error", "Please select a category.")
            return

        name = simpledialog.askstring("Input", "Enter item name:")
        if not name:
            return

        price = simpledialog.askfloat("Input", "Enter item price:")
        if price is None:
            return

        brand = simpledialog.askstring("Input", "Enter item brand:")
        if not brand:
            return

        model_year = simpledialog.askinteger("Input", "Enter item model year:")
        if model_year is None:
            return

        item_id = simpledialog.askstring("Input", "Enter item ID:")
        if not item_id:
            return

        color = simpledialog.askstring("Input", "Enter item color:")
        if not color:
            return

        item = Item(name, price, brand, model_year, item_id, color)
        categories[category_name].add_item(item)
        messagebox.showinfo("Success", f"Item added to {category_name}.")

    def view_items_in_category(self):
        category_name = self.category_listbox.get(tk.ACTIVE)
        if not category_name:
            messagebox.showwarning("Selection Error", "Please select a category.")
            return

        items = categories[category_name].items
        if not items:
            messagebox.showinfo("No Items", "No items in this category.")
            return

        items_info = "\n".join(
            f"ID: {item.id}, Name: {item.name}, Price: {item.price}, Brand: {item.brand}, Model Year: {item.model_year}, Color: {item.color}"
            for item in items)
        messagebox.showinfo(f"Items in {category_name}", items_info)

    def add_item_to_cart(self):
        category_name = self.category_listbox.get(tk.ACTIVE)
        if not category_name:
            messagebox.showwarning("Selection Error", "Please select a category.")
            return

        category = categories[category_name]
        if not category.items:
            messagebox.showinfo("No Items", "No items in this category.")
            return

        items_info = "\n".join(f"{i}: {item.name} (ID: {item.id})" for i, item in enumerate(category.items))
        item_index = simpledialog.askinteger("Input",
                                             f"Available items:\n{items_info}\nEnter item index to add to cart:")
        if item_index is None or item_index < 0 or item_index >= len(category.items):
            messagebox.showwarning("Input Error", "Invalid item index.")
            return

        item = category.items[item_index]
        cart.add_item(item)
        messagebox.showinfo("Success", f"Item '{item.name}' added to cart.")

    def view_cart(self):
        items = cart.items
        if not items:
            messagebox.showinfo("Empty Cart", "Cart is empty.")
            return

        items_info = "\n".join(
            f"ID: {item.id}, Name: {item.name}, Price: {item.price}, Brand: {item.brand}, Model Year: {item.model_year}, Color: {item.color}"
            for item in items)
        messagebox.showinfo("Cart Contents", items_info)

    def calculate_cart_total(self):
        total = cart.calculate_total()
        messagebox.showinfo("Total Cost", f"Total cart cost: {total:.2f}")

    def calculate_delivery_fee(self):
        governorate = simpledialog.askstring("Input", "Enter governorate:")
        if not governorate:
            return

        fee = cart.calculate_delivery_fee(governorate)
        messagebox.showinfo("Delivery Fee", f"Delivery fee: {fee:.2f}")
        

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]['price']
    i = low - 1
    for j in range(low, high):
        if arr[j]['price'] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

root = tk.Tk()
app = App(root)
root.geometry('800x600')
root.mainloop()
