import tkinter as tk
from tkinter import messagebox

#the user class this class i will replace it by my team class
#i had made those class for testing
#user can navigate between the items
#user can add any item to the cart
class User:
    def __init__(self,gmail,id):
        self.gmail=gmail
        self.id=gmail
        
    def navg(self):
        return self.id
    
    def add_to_cart(self,item):
        self.item=item
        return self.item
#this is the admain
#admin can add item to the app
#admain can remove any item also
class Admin:
    def __init__(self,admin_id):
        self.admin_id=admin_id
        return self.admin_id
    
    def add_item_to_app(self,add_item):
        self.add_item=add_item
        return self.add_item
    
    def remove_item(self,remo):
        self.remo=remo
        return remo

#this class inheret from user and admin
#inhert the id of the user and gmail of ther user
#in hert the admin id also
class Member(Admin,User):
    def __init__(self, admin_id,id,gmail):
        User.__init__(self,id,gmail)
        Admin.__init__(self,admin_id)
        

#the app class: make (create widgets,add_item,update_item,navigate)
#create_widgets: make the button and lable that u will click on it
#navigate: take the navg() constractor of the User and make messagebox
#add_to_cart: take the add_to_cart() constractor of the User and make messagebox
#add_item: take the add_item_to_app() constractor of the admin and make messagebox
#remove_items: take remove_item () constractor of the admin and make messagebox

class App:
    def __init__(self,root):
        self.root=root
        self.root.title("Member")
        self.member = Member("mo_aboshady", "aboshady@egmail.com", "aboshady22")
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Member interact")
        self.label.pack()
        
        self.navigate_button = tk.Button(self.root, text="Navigate", command=self.navigate)
        self.navigate_button.pack()
    
        self.add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack()
        
        self.add_item_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_item_button.pack()
        
        self.remove_item_button = tk.Button(self.root, text="Update Item", command=self.remove_items)
        self.remove_item_button.pack()
        
    
    def navigate(self):
        self.member.navg()
        messagebox.showinfo("navigate", "This catgoris")

    def add_to_cart(self):
        self.member.add_to_cart("Item")
        messagebox.showinfo("Add to cart", "Added item to cart.")

    def add_item(self):
        self.member.add_item_to_app("New Item")
        messagebox.showinfo("add item", "Added item to cart.")

    def remove_items(self):
        self.member.remove_item("Existing Item")
        messagebox.showinfo("update item", "Removed item from")

root = tk.Tk()
app = App(root)
root.geometry('500x300')
root.mainloop()